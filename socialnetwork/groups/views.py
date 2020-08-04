from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView, UpdateView, ListView
from groups.models import Group, GroupMember

# Create your views here.

class CreateGroupView(LoginRequiredMixin, CreateView): 
	fields = ('name', 'descripton')
	model = Group

class GroupDetailView(DetailView): 
	template_name = 'groups/group_detail.html'
	model = Group
	def get_object(self):
		object = get_object_or_404(Group, slug=self.kwargs['slug'])
		return object

class GroupListView(ListView): 
	model = Group 


