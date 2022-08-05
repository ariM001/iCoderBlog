from django.urls import path   # include is added manually
from . import views  # added manually

urlpatterns = [
    path('', views.home, name='home'),  # added manually
    path('search/', views.search, name='search'),  # added manually
    path('contact/', views.contact, name='contact'),  # added manually
    path('about/', views.about, name='about'),  # added manually
    path('signup/', views.handleSignup,
         name='handleSignup')  # added manually
]
