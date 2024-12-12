from django.contrib import admin
from .models import Destination, Tour, Customer, Booking, Review

admin.site.register(Destination)
admin.site.register(Tour)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Review)