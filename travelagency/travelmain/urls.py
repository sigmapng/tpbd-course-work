from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:tour_id>/book/', views.create_booking, name='create_booking'),
    path('booking/success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('tour/<int:tour_id>/review/', views.add_review, name='add_review'),
]