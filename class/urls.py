from django.urls import path
from . import views

urlpatterns = [
    path('class', views.class_list, name='class'),
    path('book-seat/', views.book_seat, name='book_seat'),
]
