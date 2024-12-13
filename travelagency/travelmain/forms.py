from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Review, Tour


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_people', 'date', 'number_of_days']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'country', 'city',
                  'image', 'price', 'start_date', 'end_date']
