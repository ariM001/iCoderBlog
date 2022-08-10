from django.urls import path

from . import views  # added manually

urlpatterns = [
    #  API to post a comment
    path('postComment/', views.postComment, name='postComment'),   # this url pattern is placed at top , otherwise it will be considered as a slug


    # urlpatterns for handling blog home and blog post
    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>/', views.BlogPost, name='BlogPost'),

]
