from django.urls import path

from . import views  # added manually

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>/', views.BlogPost, name='BlogPost'),
]
