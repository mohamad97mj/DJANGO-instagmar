from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class MyUser(User):
    fullname = models.CharField(max_length=50)
    followings = models.ManyToManyField('MyUser', related_name='followers')

    def __str__(self):
        return self.fullname


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.ImageField(upload_to='instagmar_app')
    caption = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField()
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateField()
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
