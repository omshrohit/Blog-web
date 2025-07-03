from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .froms import UserSignupForm
# Create your views here.

class UserRegistration(CreateView):
    # form_class = UserCreationForm
    form_class = UserSignupForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("posts")
