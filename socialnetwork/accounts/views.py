from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from . import forms

# Create your views here.

class HomePage(TemplateView): 
	template_name = 'accounts/index.html'

class SignUp(CreateView): 
	form_class = forms.CreateUserForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'
	