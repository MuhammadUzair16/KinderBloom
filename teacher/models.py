# models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/')
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
