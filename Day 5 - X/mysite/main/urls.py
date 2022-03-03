from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
]
