import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")
django.setup()

from images.models import Gene, Antibody, Image

def populate():
    wb_dir = '/home/btpf/cropped-IB'  # Change to the correct path
    ip_dir = '/home/btpf/cropped-IP'  # Change to the correct path

    # Process Western Blot images
    for gene_dir in os.listdir(wb_dir):
        gene_path = os.path.join(wb_dir, gene_dir)
        if os.path.isdir(gene_path):
            gene, created = Gene.objects.get_or_create(name=gene_dir)
            
            for filename in os.listdir(gene_path):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    antibody_name = filename.split('_')[0]  # Adjust based on your naming convention
                    antibody, created = Antibody.objects.get_or_create(name=antibody_name, gene=gene)
                    image_path = os.path.join(gene_path, filename)
                    Image.objects.create(
                        antibody=antibody,
                        image_type='WB',
                        image_path=image_path
                    )

    # Process Immunoprecipitation images
    for gene_dir in os.listdir(ip_dir):
        gene_path = os.path.join(ip_dir, gene_dir)
        if os.path.isdir(gene_path):
            gene, created = Gene.objects.get_or_create(name=gene_dir)
            
            for filename in os.listdir(gene_path):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    antibody_name = filename.split('_')[0]  # Adjust based on your naming convention
                    antibody, created = Antibody.objects.get_or_create(name=antibody_name, gene=gene)
                    image_path = os.path.join(gene_path, filename)
                    Image.objects.create(
                        antibody=antibody,
                        image_type='IP',
                        image_path=image_path
                    )

if __name__ == '__main__':
    populate()
