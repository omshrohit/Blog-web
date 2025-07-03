from django import forms
from . models import Post,Category
# choices =[('coding','coding'),('sports','sports'),('intertainments','intertainments')]
choices = Category.objects.all().values_list('name','name')
choices_list=[]
for cats in choices:
    choices_list.append(cats)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body')

        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'writer','type':'hidden'}),
            'category' : forms.Select(choices=choices_list,attrs={'class':'form-control',}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }


#update post form
class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body')

        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }