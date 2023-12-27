from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.user_login.as_view(), name='user_login'),
    path('logout/', views.user_logout.as_view(), name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),
]