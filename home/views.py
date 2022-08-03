from django.shortcuts import render

from home.models import Contact  # added manually
from django.contrib import messages # added manually

# Create your views here.
def home(request):
    return render(request, "home/home.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        if len(name)<4 or len(email)<10 or len(phone)<10 or len(content)<10:
            messages.error(request, 'Please fill all the fields correctly!')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your message has been sent successfully!')
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")
