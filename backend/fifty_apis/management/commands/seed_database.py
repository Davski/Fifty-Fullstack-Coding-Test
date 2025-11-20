from django.core.management.base import BaseCommand
from fifty_apis.models import User, Sensor

class Command(BaseCommand):
    help = "Seed initial data of users and sensors"

    def handle(self, *args, **options):
        User.objects.seed_data()
        Sensor.objects.seed_data()
        self.stdout.write(self.style.SUCCESS("Seeded user and sensors into the database."))
