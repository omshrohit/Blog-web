from django.shortcuts import render,get_object_or_404,HttpResponse
from . models import Post,Category
from django.views.generic import ListView , DeleteView , CreateView , UpdateView , DeleteView
from . forms import BlogPostForm,UpdateBlogPostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.core.cache import cache
from django.contrib.auth.models import User
# Create your views here.
# def getIpAddress(request):
#     user_ip=request.META.get("HTTP_X_FORWARDED_FOR")
#     if user_ip is not None:
#         ip=user_ip.split(",")[0]
#     else:
#         ip=request.META.get('REMOTE_ADDR')
#     return HttpResponse("wellcome User your ip address is {}".format(ip))
def get_user_info(request,pk):
    query=User.objects.get(id=pk)
    ip=request.session.get('ip',0)
    ct=cache.get('count',version=request.user.pk)
    # return HttpResponse("<h1>user ip is {}</br> Login count : {},{}".format(ip,ct,query))
    return render(request,'userinfo.html',{'query':query,'ct':ct,'ip':ip})

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get("post_id"))
    post.like.add(request.user)
    return HttpResponse(reverse('detail-post',args=[str(pk)]))

class AddCategoryView(CreateView):
    model = Category
    template_name = 'create-category.html'
    fields = '__all__'

def CategoryView(request,cats):
    query = Post.objects.filter(category=cats.replace("-"," "))
    return render(request,'categories.html',{'categories_posts':query,'cats':cats.title().replace("-"," ")})

    def get_context_data(self,*args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(CategoryView,self).get_context_data(*args,**kwargs)

        context['cats_menu']=cats_menu
        return context

def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request,'category_list.html',{'category_list':category_list})

class AllBlogPosts(ListView):
    model = Post
    template_name = 'index.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self,*args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(AllBlogPosts,self).get_context_data(*args,**kwargs)
        context['cats_menu']=cats_menu
        return context
   

class DetailsBlogPost(DeleteView):
    model = Post
    template_name = 'detail-post.html'

    def get_context_data(self,*args,**kwargs):
        cats_menu = Category.objects.all()
        context = super(DetailsBlogPost,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['cats_menu']=cats_menu
        context['total_likes']=total_likes
        return context

class AddBlogPost(CreateView):
    model = Post
    template_name = 'create-post.html'
    # fields = '__all__'
    form_class = BlogPostForm

class UpdateBlogPost(UpdateView):
    model = Post
    template_name = 'update-post.html'
    # fields = ('title','title_tag','body')
    form_class = UpdateBlogPostForm
  

class DeleteBlogPost(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy("posts")

