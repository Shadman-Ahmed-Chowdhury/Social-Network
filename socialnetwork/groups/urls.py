from django.contrib import admin
from django.urls import path, include
from . import views 
from .views import GroupDetailView, GroupListView, CreateGroupView

urlpatterns = [
   	path('<slug>/', GroupDetailView.as_view(), name='group-detail'), 
]
