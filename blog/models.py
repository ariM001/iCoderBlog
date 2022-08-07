from django.db import models
from django.contrib.auth.models import User     # added manually
from django.utils.timezone import now           # added manually

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


class BlogComment(models.Model):    #😃
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:25] + "..." + " By " + self.user.username 
    