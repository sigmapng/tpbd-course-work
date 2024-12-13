from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Tour, Review, Customer
from .forms import BookingForm, ReviewForm, UserRegisterForm, TourForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'travelmain/tour_list.html', {'tours': tours})


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
            user = form.save()
            Customer.objects.create(user=user, first_name=user.username)
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
            return redirect('tour_list')
    else:
        form = AuthenticationForm()
    return render(request, 'travelmain/login.html', {'form': form})


@login_required
def user_logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def create_booking(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour
            booking.customer = request.user
            booking.total_price = booking.number_of_people * \
                tour.price * booking.number_of_days
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


@login_required
def bookings_panel(request):
    if not request.user.is_staff:
        return redirect('tour_list')
    bookings = Booking.objects.all()
    return render(request, 'travelmain/admin_actions/bookings_panel.html', {'bookings': bookings})


@login_required
def tours_panel(request):
    if not request.user.is_staff:
        return redirect('tour_list')
    tours = Tour.objects.all()
    add_tour_form = TourForm()
    for tour in tours:
        tour.get_edit_form = TourForm(instance=tour)
    return render(request, 'travelmain/admin_actions/tours_panel.html', {'tours': tours, 'add_tour_form': add_tour_form})


@login_required
def users_panel(request):
    if not request.user.is_staff:
        return redirect('tour_list')
    users = Customer.objects.all()
    add_user_form = UserRegisterForm()
    return render(request, 'travelmain/admin_actions/users_panel.html', {'users': users, 'add_user_form': add_user_form})


@login_required
def delete_booking(request, booking_id):
    if not request.user.is_staff:
        return redirect('tour_list')
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
    else:
        form = TourForm(instance=tour)
    return render(request, 'travelmain/admin_actions/edit_tour.html', {'form': form, 'tour': tour})


@login_required
def delete_tour(request, tour_id):
    if not request.user.is_staff:
        return redirect('tour_list')
    tour = get_object_or_404(Tour, id=tour_id)
    tour.delete()
    return redirect('tours_panel')


@login_required
def add_tour(request):
    if not request.user.is_staff:
        return redirect('tour_list')
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours_panel')
    return redirect('tours_panel')


@login_required
def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect('tour_list')
    user = get_object_or_404(Customer, id=user_id)
    user.delete()
    return redirect('users_panel')


@login_required
def add_user(request):
    if not request.user.is_staff:
        return redirect('tour_list')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user, first_name=user.username)
            return redirect('users_panel')
    return redirect('users_panel')
