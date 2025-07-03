from django.contrib import admin
from django.urls import path,include
from . views import UserRegistration
urlpatterns = [
  path("register",UserRegistration.as_view(),name="register")
]