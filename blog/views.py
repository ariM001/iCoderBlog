from django.shortcuts import render,redirect
from .models import Post, BlogComment          # added manually
from django.contrib import messages            # added manually
# Create your views here.


def BlogHome(request):
    posts = Post.objects.all()
    params = {"posts": posts}
    return render(request, "blog/blogHome.html", params)


def BlogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post = post)
    params = {'post': post, 'comments':comments}
    return render(request, "blog/blogPost.html", params)


def postComment(request):
    if request.method == "POST":    
        comment = request.POST["comment"]
        user = request.user
        postSno = request.POST["postSno"] 
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request,"Comment added successfully")
        
    return redirect(f'/blog/{post.slug}')