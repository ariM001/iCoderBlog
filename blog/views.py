from django.shortcuts import render
from django.http import HttpResponse  # added manually
from .models import Post          # added manually
# Create your views here.


def BlogHome(request):
    posts = Post.objects.all()
    params = {"posts": posts}
    return render(request, "blog/blogHome.html", params)


def BlogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    return render(request, "blog/blogPost.html", {'post': post})
