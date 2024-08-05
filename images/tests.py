from django.test import TestCase
from django.shortcuts import render
from .models import Antibody

def browse(request):
    antibodies = Antibody.objects.all().prefetch_related('image_set')
    return render(request, 'images/browse.html', {'antibodies': antibodies})
