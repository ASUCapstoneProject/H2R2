from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    is_user = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    email = models.EmailField(max_length = 254, default=None)

    def __str__(self):
        id = self.id
        return f'{self.username}'

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user}'

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
        ordering = ['-created']

class WaterQuality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=200)
    pH_value = models.DecimalField(max_digits=4, decimal_places=2) # pH value
    hardness = models.IntegerField() # Hardness
    TDS = models.IntegerField() # Total Dissolved Solids (TDS)
    chloramines = models.DecimalField(max_digits=4, decimal_places=2) # Chloramines
    sulfate = models.DecimalField(max_digits=4, decimal_places=2) # Sulfate
    conductivity = models.DecimalField(max_digits=4, decimal_places=2) # Conductivity
    organic_carbon = models.DecimalField(max_digits=4, decimal_places=2) # Organic Carbon (TOC)
    trihalomethanes = models.DecimalField(max_digits=4, decimal_places=2) # Trihalomethanes (THMs)
    turbidity = models.DecimalField(max_digits=4, decimal_places=2) # Turbidity

    def __str__(self):
        return f'Water quality for {self.company}'