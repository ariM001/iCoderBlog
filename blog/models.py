from django.db import models

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="blog/post_images", default="")
    slug = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " By " + self.author + " (Published On " + str(self.timeStamp) + ")"


# recuired fields to handle comments in our blog
# sno
# comment
# user
# post
# parent
# timestamp
class Comment(models.Model):    #😃
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=2000)
    user = models.CharField(max_length=500) 
    post = models.CharField(max_length=500)
    parent = models.CharField(max_length=500)
    timeStamp = models.DateTimeField(blank=True)