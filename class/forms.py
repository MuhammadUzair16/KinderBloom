from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['class_booked', 'name', 'email']
        widgets = {
            'class_booked': forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px'}),
            'name': forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Your Email'}),
        }
