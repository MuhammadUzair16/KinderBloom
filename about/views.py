# views.py
from django.shortcuts import render
from .models import AboutUs

def about_us(request):
    about_content = AboutUs.objects.all()
    return render(request, 'about/about.html', {'about_content': about_content})
