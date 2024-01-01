from django.db import models

class AddPhoto(models.Model):
    user_id = models.IntegerField()
    title=models.CharField(default="",max_length=100)
    image=models.CharField(default="",max_length=1000)
    description=models.CharField(default="",max_length=1000)
    anything=models.CharField(default="",max_length=1000)

class User(models.Model):
    username=models.CharField(default="",max_length=100)
    image=models.TextField(default="")
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)


