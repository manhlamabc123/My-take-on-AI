from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.blank, name="edit_profile"),
    path('change_password/', views.blank, name="change_password"),
]
