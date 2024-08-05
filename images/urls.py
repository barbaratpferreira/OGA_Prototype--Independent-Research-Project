from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('browse/', views.browse, name='browse'),
    path('gene/<int:gene_id>/', views.gene_detail, name='gene_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
]




