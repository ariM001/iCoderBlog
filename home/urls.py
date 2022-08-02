from django.urls import path   # include is added manually
from . import views # added manually

urlpatterns = [
    path('', views.home, name='Home'), # added manually
    path('contact/', views.contact, name='Contact') , # added manually
    path('about/', views.about, name='About')  # added manually
]
