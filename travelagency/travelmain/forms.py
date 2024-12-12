from django import forms
from .models import Booking, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'number_of_people']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer', 'rating', 'comment']
