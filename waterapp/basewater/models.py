from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_user = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)