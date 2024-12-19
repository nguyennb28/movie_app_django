from django.core.management.base import BaseCommand
from movie_app.models import Gallery, Categories
from faker import Faker
import random
import os

class Command(BaseCommand):
    help = 'Seed the Gallery model with predefined data'
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = Categories.objects.all()
        
        for _ in range(10):
            image_name = random.choice(os.listdir('media/gallery'))
            video_name = random.choice(os.listdir('media/video'))
            Gallery.objects.create(
                image=f"gallery/{image_name}",
                title=fake.sentence(),
                description=fake.paragraph(),
                video=f"video/{video_name}",
                category=random.choice(categories)
            )
            
        self.stdout.write(self.style.SUCCESS('Gallery created successfully!'))