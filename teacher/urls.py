# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team_view, name='team'),
]
