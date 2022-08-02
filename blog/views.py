from django.shortcuts import render
from django.http import HttpResponse  # added manually

# Create your views here.


def BlogHome(request):
    return HttpResponse("Blog Home")


def BlogPost(request, slug):
    return HttpResponse(f"Blog Post : {slug}")
