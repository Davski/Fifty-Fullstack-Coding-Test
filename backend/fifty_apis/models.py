from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your managers here.
class UserSeedManager(UserManager):
    def seed_data(self):
        user, created = self.get_or_create(username='one_user', email='one@user.com')
        if created:
            user.set_password('password')
            user.save()
        return user

class SensorSeedManager(UserManager):
    def seed_data(self):
        user = User.objects.get(username='one_user')

        sensors = [
            {'name': 'device-001', 'description': 'Predefined Sensor', 'model': 'EnviroSense'},
            {'name': 'device-002', 'description': 'Predefined Sensor', 'model': 'ClimaTrack'},
            {'name': 'device-003', 'description': 'Predefined Sensor', 'model': 'AeroMonitor'},
            {'name': 'device-004', 'description': 'Predefined Sensor', 'model': 'HydroTherm'},
            {'name': 'device-005', 'description': 'Predefined Sensor', 'model': 'EcoStat'},
        ]

        for sensor in sensors:
            self.get_or_create(
                owner=user,
                name=sensor['name'],
                description=sensor['description'],
                model=sensor['model'],
            )

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    objects = UserSeedManager()

    def __str__(self):
        return self.username

class Sensor(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    model = models.CharField()

    objects = SensorSeedManager()

    def __str__(self):
        return self.name + ' ' + self.description

class Reading(models.Model):
    timestamp = models.DateTimeField()
    sensor = models.CharField()
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + ': temperature: ' + self.temperature + ': humidity: ' + self.humidity + ': time: ' + self.timestamp

    class Meta:
        indexes = [
            models.Index(fields=['sensor','timestamp']),
        ]
        models.UniqueConstraint(fields=['sensor', 'timestamp'], name='unique_together')
