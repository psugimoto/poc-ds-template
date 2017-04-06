from django.core.management.base import BaseCommand

from iris import models

class Command(BaseCommand):
    help = "Train the IRIS classifier."

    def handle(self, *args, **options):
        print('Training a model.')
        models.train()
        print('Saving the trained model.')
        models.save_model()
