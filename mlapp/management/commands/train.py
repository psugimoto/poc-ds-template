from django.core.management.base import BaseCommand

from mlapp import models

class Command(BaseCommand):
    help = "Train the Machine Learning Model."

    def handle(self, *args, **options):
        print('Training a model.')
        models.train()
        print('Saving the trained model.')
        models.save_model()
