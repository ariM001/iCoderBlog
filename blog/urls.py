from django.urls import path

from . import views  # added manually

urlpatterns = [
    #  API to post a comment
    path('postComment/', views.postComment, name='postComment'),

    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>/', views.BlogPost, name='BlogPost'),

]
