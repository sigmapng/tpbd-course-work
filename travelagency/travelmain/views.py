from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Tour, Review, Destination, Customer
from .forms import BookingForm, ReviewForm, UserRegisterForm, TourForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# General views


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'travelmain/destination_list.html', {'destinations': destinations})


def about_us(request):
    return render(request, 'travelmain/about_us.html')


def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    reviews = tour.reviews.all()
    return render(request, 'travelmain/tour_detail.html', {'tour': tour, 'reviews': reviews})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'travelmain/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('destination_list')
    else:
        form = AuthenticationForm()
    return render(request, 'travelmain/login.html', {'form': form})


@login_required
def user_logout_view(request):
    logout(request)
    return redirect('login')

# Admin views


@login_required
def bookings_panel(request):
    if not request.user.is_staff:
        return redirect('destination_list')
    bookings = Booking.objects.all()
    return render(request, 'travelmain/admin_actions/bookings_panel.html', {'bookings': bookings})


@login_required
def tours_panel(request):
    if not request.user.is_staff:
        return redirect('destination_list')
    tours = Tour.objects.all()
    add_tour_form = TourForm()
    for tour in tours:
        tour.get_edit_form = TourForm(instance=tour)
    return render(request, 'travelmain/admin_actions/tours_panel.html', {'tours': tours, 'add_tour_form': add_tour_form})


@login_required
def users_panel(request):
    if not request.user.is_staff:
        return redirect('destination_list')
    users = Customer.objects.all()
    add_user_form = UserRegisterForm()
    for user in users:
        user.get_edit_form = UserRegisterForm(instance=user)
    return render(request, 'travelmain/admin_actions/users_panel.html', {'users': users, 'add_user_form': add_user_form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('bookings_panel')


@login_required
def edit_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tours_panel')
    return redirect('tours_panel')


@login_required
def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    tour.delete()
    return redirect('tours_panel')


@login_required
def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours_panel')
    return redirect('tours_panel')


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(Customer, id=user_id)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_panel')
    return redirect('users_panel')


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(Customer, id=user_id)
    user.delete()
    return redirect('users_panel')


@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_panel')
    return redirect('users_panel')

# User views


@login_required
def create_booking(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.customer = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'travelmain/user_actions/create_booking.html', {'form': form, 'tour': tour})


@login_required
def booking_success(request):
    return render(request, 'travelmain/user_actions/booking_success.html')


@login_required
def add_review(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.customer = request.user
            review.save()
            return redirect('tour_detail', tour_id=tour.id)
    else:
        form = ReviewForm()
    return render(request, 'travelmain/user_actions/add_review.html', {'form': form, 'tour': tour})


@login_required
def manage_bookings(request):
    bookings = Booking.objects.filter(customer=request.user)
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = get_object_or_404(
            Booking, id=booking_id, customer=request.user)
        booking.delete()
        return redirect('manage_bookings')
    return render(request, 'travelmain/user_actions/manage_bookings.html', {'bookings': bookings})
