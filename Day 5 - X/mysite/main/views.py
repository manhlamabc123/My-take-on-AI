from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    user = response.user
    member = Member.objects.get(user_id = user.id)
    return render(response, "main/profile.html", {"user": user, "member": member})

def edit_profile(response):
    return render(response, "main/edit_profile.html", {})

def change_password(response):
    return render(response, "main/change_password.html", {})