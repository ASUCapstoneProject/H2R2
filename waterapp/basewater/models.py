from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    is_user = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200, default=None)
    dec = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']