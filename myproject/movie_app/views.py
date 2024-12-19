from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Gallery

# Create your views here.
def home(request):
    return render(request, 'homepage/index.html')

def gallery(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery/index.html', {'galleries': galleries})