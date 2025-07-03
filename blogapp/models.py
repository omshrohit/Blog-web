from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("posts")


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=250,default='coding...')
    like = models.ManyToManyField(User,related_name="blog_post")
    

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title +' | '+ str(self.author)
    

    def get_absolute_url(self):
        return reverse("posts")
