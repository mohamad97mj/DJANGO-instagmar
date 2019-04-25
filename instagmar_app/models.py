from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserModel(User):
    fullname = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname


class PostModel(models.Model):
    content = models.ImageField()
    caption = models.TextField()


class CommentModel(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    related_post = models.ForeignKey(PostModel, on_delete=models.CASCADE)


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    related_post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
