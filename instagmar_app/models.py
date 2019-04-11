from django.db import models

# Create your models here.


class UserModel(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=25)
