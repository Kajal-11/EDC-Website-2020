from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as core_views
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('navbar/',		views.NavBar),
    path('signup/', core_views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('profile/', core_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('',			views.home,		name='home'),
    path('our-team/',	views.team,	name='our-team'),
]
