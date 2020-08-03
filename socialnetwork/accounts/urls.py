from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'), 
    path('login/', 
    	auth_views.LoginView.as_view(template_name='accounts/login.html'), 
    	name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('signup/', views.SignUp.as_view(), name='signup'),

]
