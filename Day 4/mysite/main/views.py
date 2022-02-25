from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(respone):
    return HttpResponse('<h1>Hello world!</h1>')

def v1(respone):
    return HttpResponse('<h1>View 1</h1>')