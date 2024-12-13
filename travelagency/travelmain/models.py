from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default='Unknown Country')
    city = models.CharField(max_length=100, default='Unknown City')
    image = models.ImageField(upload_to='tours/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()
    number_of_days = models.IntegerField(default=1)
    date = models.DateField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.customer.username} for {self.tour.name}"


class Review(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.username} for {self.tour.name}"
