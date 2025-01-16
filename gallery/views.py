from django.shortcuts import render
from .models import Category, GalleryImage

def gallery_view(request):
    categories = Category.objects.all()
    images = GalleryImage.objects.select_related('category')
    return render(request, 'gallery/gallery.html', {'categories': categories, 'images': images})
