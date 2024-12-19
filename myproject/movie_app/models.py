from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gallery(models.Model):
    # title
    # description
    # image
    # category
    # created_at
    # updated_at
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/', default='gallery/1.jpg')
    video = models.FileField(upload_to='video/', null=True, blank=True, default='video/1mns.mp4')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title or f"Image {self.id}"
    