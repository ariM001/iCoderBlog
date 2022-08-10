from django.shortcuts import render,redirect, HttpResponse
from .models import Post, BlogComment          # added manually
from django.contrib import messages            # added manually



def BlogHome(request):
    posts = Post.objects.all()
    params = {"posts": posts}
    return render(request, "blog/blogHome.html", params)


def BlogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post = post, parent=None)   # these are parent comments
    replies = BlogComment.objects.filter(post = post).exclude(parent=None)  # these are replies ( all comments - parent comments)

    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    params = {'post': post, 'comments':comments, 'replyDict':replyDict}
    return render(request, "blog/blogPost.html", params)


def postComment(request):
    if request.method == "POST":    
        comment = request.POST["comment"]
        postSno = request.POST["postSno"] 
        post = Post.objects.get(sno=postSno)   # finding the particular post with its sno
        parentSno = request.POST["parentSno"]
        user = request.user

        # when it is a parent comment itself
        if parentSno == "":                
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request,"Comment added successfully")
        
        # when it is a child comment , here parentSno is not null
        else:                               
            parent = BlogComment.objects.get(sno=parentSno)    # finding the particular comment with its sno
            reply = BlogComment(comment=comment, user=user, post=post, parent=parent)
            reply.save()
            messages.success(request,"Reply added successfully")
        
        return redirect(f'/blog/{post.slug}')
    
    else:
       return HttpResponse("404 Not Found!")
