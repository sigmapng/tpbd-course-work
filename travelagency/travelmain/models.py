from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tours', null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Set default value here
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_people = models.IntegerField()
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
