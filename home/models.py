import email
from django.db import models

# Create your models here.
# Database --> Excel workbook
# Models in Django --> Database Table --> Excel sheet

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    phone = models.CharField(max_length=12)
    content = models.TextField(max_length=1000)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return self.name + " - " + self.email
    

