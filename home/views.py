from django.shortcuts import render, redirect, HttpResponse

from home.models import Contact  # added manually
from django.contrib import messages  # added manually
from blog.models import Post  # added manually
from django.contrib.auth.models import User  # added manually to add user in database
from django.contrib.auth import authenticate, login, logout     # added manually


# Create your views here.

def home(request):
    return render(request, "home/home.html")


def search(request):
    query = request.GET["query"]
    if len(query) > 60 or len(query) == 0:
        posts = Post.objects.none()

    else:
        postsTitle = Post.objects.filter(title__icontains=query)
        postsContent = Post.objects.filter(content__icontains=query)
        postsAuthor = Post.objects.filter(author__icontains=query)
        posts = postsTitle.union(postsContent).union(postsAuthor)

    if posts.count() == 0:
        messages.warning(
            request, "No results found! Please search with related queries"
        )

    params = {"posts": posts, "query": query}
    return render(request, "home/search.html", params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        if len(name) < 4 or len(email) < 10 or len(phone) < 10 or len(content) < 10:
            messages.error(request, "Please fill all the fields correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


def handleSignup(request):
    if request.method == "POST":
        # Obtaining the post parameters
        print(request.POST)
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # check for erroneous inputs
        # usename should be under 10 characters
        if len(username) > 10:
            messages.error(request, "Max length of username is 10")
            return redirect("home")

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username can contain only letters and numbers")
            return redirect("home")

        # username should be lowercase
        for i in username:
            if (not i.isnumeric()) and (i == i.upper()):
                messages.error(
                    request, "Username should not contain any uppercase characters"
                )
                return redirect("home")

        # both the password hould match
        if pass1 != pass2:
            messages.error(request, "Passwords mismatched")
            return redirect("home")

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCoder account has been successfully created")
        return redirect("home")
    else:
        return HttpResponse("404 Not Found!")


def handleLogin(request):
    # get the request parameters
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpass = request.POST["loginpass"]

        user = authenticate(username = loginusername, password = loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, please try again")
            return redirect('home')

    else:
       return HttpResponse("404 Not Found!")

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


