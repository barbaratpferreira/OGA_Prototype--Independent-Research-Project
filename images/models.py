# images/models.py

from django.db import models

def image_upload_path(instance, filename):
    if instance.image_type == 'WB':
        return f'cropped_IB/{instance.antibody.gene.name}/{filename}'
    elif instance.image_type == 'IP':
        return f'cropped_IP/{instance.antibody.gene.name}/{filename}'

class Gene(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Antibody(models.Model):
    name = models.CharField(max_length=100)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Image(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('cropped_IB', 'Western Blot'),
        ('cropped_IP', 'Immunoprecipitation'),
    ]
    antibody = models.ForeignKey(Antibody, on_delete=models.CASCADE)
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
    image = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return f"{self.antibody.name} - {self.get_image_type_display()}"
