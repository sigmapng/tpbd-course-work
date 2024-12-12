from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Destination, Tour, Booking, Review
from .forms import BookingForm, ReviewForm

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'travelmain/destination_list.html', {'destinations': destinations})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    reviews = Review.objects.filter(tour=tour)
    return render(request, 'travelmain/tour_detail.html', {'tour': tour, 'reviews': reviews})

def create_booking(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.total_price = tour.price * booking.number_of_people
            booking.save()
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'travelmain/create_booking.html', {'form': form, 'tour': tour})

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'travelmain/booking_success.html', {'booking': booking})

def add_review(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.save()
            return redirect('tour_detail', tour_id=tour.id)
    else:
        form = ReviewForm()
    return render(request, 'travelmain/add_review.html', {'form': form, 'tour': tour})
