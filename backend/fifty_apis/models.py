from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

# class Readings(models.Model):
#     sensor = models.CharField()
#     temperature = models.DecimalField(max_digits=5, decimal_places=2)
#     humidity = models.DecimalField(max_digits=5, decimal_places=2)
#     timestamp = models.DateTimeField()
