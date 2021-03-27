from django.db import models

# Create your models here.

# class postdata(models.Model):
#     eventname = models.CharField(max_length=30)
#     desc = models.TextField(max_length=100)
#     time = models.TimeField(auto_now_add=True)
#     location = models.CharField(max_length=15)
    
class postds(models.Model):
    eventname = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=15) 
    image = models.ImageField(upload_to='images/')
    
