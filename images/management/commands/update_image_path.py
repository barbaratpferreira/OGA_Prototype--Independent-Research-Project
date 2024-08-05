# scripts/management/commands/update_image_paths.py

from django.core.management.base import BaseCommand
from images.models import Image

class Command(BaseCommand):
    help = 'Update image paths to be relative to media directory'

    def handle(self, *args, **kwargs):
        images = Image.objects.all()
        for image in images:
            if image.image_path.startswith('/home/btpf/'):
                # Update the path to be relative
                image.image_path = image.image_path.replace('/home/btpf/', '')
                image.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated image paths'))
