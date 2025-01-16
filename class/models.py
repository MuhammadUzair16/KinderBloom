from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    age_group = models.CharField(max_length=50)
    total_seats = models.PositiveIntegerField()
    class_time = models.CharField(max_length=50)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    class_booked = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.class_booked.name}"


