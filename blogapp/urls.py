from django.contrib import admin
from django.urls import path
from .views import AllBlogPosts,DetailsBlogPost,AddBlogPost,UpdateBlogPost,DeleteBlogPost,AddCategoryView,CategoryView,CategoryListView,LikeView
from .views import get_user_info
urlpatterns = [
   path("",AllBlogPosts.as_view(),name='posts'),
   path("detail-post/<int:pk>/",DetailsBlogPost.as_view(),name='detail-post'),
   path("category-posts/<str:cats>/",CategoryView,name='categories'),
   path("create-post/",AddBlogPost.as_view(),name='create-post'),
   path("crete-category/",AddCategoryView.as_view(),name='create-category'),
   path("edit-post/<int:pk>/",UpdateBlogPost.as_view(),name='edit-post'),
   path("delete-post/<int:pk>/",DeleteBlogPost.as_view(),name="delete-post"),
   path("category-list/",CategoryListView,name='category-lists'),
   path("like/<int:pk>/",LikeView,name="like"),
   # path("ipaddress/",getIpAddress,name="getIpAddress"),
   path("ipaddressUsingSession/<int:pk>/",get_user_info,name="get_user_info")
]