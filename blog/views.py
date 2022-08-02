from django.shortcuts import render
from django.http import HttpResponse  # added manually

# Create your views here.


def BlogHome(request):
    return render(request, "blog/blogHome.html")


def BlogPost(request, slug):
    params = {'slug':slug}
    return render(request, "blog/blogPost.html", params)

