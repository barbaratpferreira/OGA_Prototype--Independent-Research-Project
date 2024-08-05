from django.shortcuts import render, get_object_or_404
from .models import Gene, Antibody
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'images/home.html')

def browse(request):
    genes = Gene.objects.all().order_by('name')
    context = {
        'genes': genes,
    }
    return render(request, 'images/browse.html', context)


def about(request):
    return render(request, 'images/about.html')

def signin(request):
    return render(request, 'images/signin.html')

def gene_detail(request, gene_id):
    gene = get_object_or_404(Gene, id=gene_id)
    antibodies = Antibody.objects.filter(gene=gene).prefetch_related('image_set')
    image_path = f'tables/{gene.name}.png'


    full_path = os.path.join(settings.MEDIA_ROOT, image_path)
    file_exists = os.path.isfile(full_path)

    # Print debugging information
    print(f"Gene name: {gene.name}")
    print(f"Image path: {image_path}")
    print(f"Full path: {full_path}")
    print(f"File exists: {file_exists}")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"MEDIA_URL: {settings.MEDIA_URL}")

    context = {
        'gene': gene,
        'antibodies': antibodies,
        'image_path': image_path,
        'file_exists': file_exists,
        'full_path': full_path, 
        'media_url': settings.MEDIA_URL,  
    }
    return render(request, 'images/gene_detail.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send email
        send_mail(
            f'New contact from {name}',
            f'From: {email}\n\nMessage:\n{message}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],  
            fail_silently=False,
        )
        
        
        return redirect('contact_success')
    return render(request, 'images/contact.html')

def contact_success(request):
    return render(request, 'images/contact_success.html')
