from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
