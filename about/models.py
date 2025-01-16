from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    small_image = models.ImageField(upload_to='about_images/', default='about_images/default_small_image.jpg')

    def __str__(self):
        return self.title


