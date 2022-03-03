from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    user = response.user
    return render(response, "main/profile.html", {"user": user})

def edit_profile(response):
    return render(response, "main/edit_profile.html", {})

def change_password(response):
    return render(response, "main/change_password.html", {})