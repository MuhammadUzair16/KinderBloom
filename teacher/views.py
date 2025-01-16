# views.py
from django.shortcuts import render
from .models import Teacher

def team_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/team.html', {'teachers': teachers})
