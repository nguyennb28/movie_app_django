from django.core.management.base import BaseCommand
from movie_app.models import Categories

class Command(BaseCommand):
    help = 'Seed the Categories model with predefined data'
    
    def handle(self, *args, **kwargs):
        data = [
            {
                'name': 'Category 1',
                'description': 'Description 1'
            },
            {
                'name': 'Category 2',
                'description': 'Description 2'
            },
            {
                'name': 'Category 3',
                'description': 'Description 3'
            },
            {
                'name': 'Category 4',
                'description': 'Description 4'
            },
            {
                'name': 'Category 5',
                'description': 'Description 5'
            },
        ]
        
        for item in data:
            Categories.objects.create(**item)
            
        self.stdout.write(self.style.SUCCESS('Categories created successfully!'))