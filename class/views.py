from django.shortcuts import render, get_object_or_404, redirect
from .models import Class
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class/class_list.html', {'classes': classes})


def book_seat(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            booking = form.save()

            # Send confirmation email to the user
            send_mail(
                'Booking Confirmation',
                f'Thank you for booking a seat for {booking.class_booked.name}. Your seat has been reserved!',
                settings.EMAIL_HOST_USER,  # Sender email address
                [booking.email],  # Recipient email address
                fail_silently=False,
            )

            # Redirect to the class page (or any other page)
            return redirect('class')
    else:
        form = BookingForm()

    return render(request, 'class/book_seat.html', {'form': form})

