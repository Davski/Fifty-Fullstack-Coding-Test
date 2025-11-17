from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Sensor(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    model = models.CharField()

    def __str__(self):
        return self.name + ' ' + self.description

class Reading(models.Model):
    timestamp = models.DateTimeField()
    sensor = models.CharField()
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + ' ' + self.temperature + ' ' + self.humidity + ' ' + self.timestamp

    class Meta:
        indexes = [
            models.Index(fields=["sensor","timestamp"]),
        ]
        models.UniqueConstraint(fields=["sensor", "timestamp"], name="unique_together")
