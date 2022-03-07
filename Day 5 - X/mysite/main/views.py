from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    user = response.user
    return render(response, "main/profile.html", {"user": user})

def blank(response):
    return render(response, "main/blank.html", {})