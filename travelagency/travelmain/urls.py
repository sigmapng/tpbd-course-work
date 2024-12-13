from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('about-us/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('manager/bookings/', views.bookings_panel, name='bookings_panel'),
    path('manager/tours/', views.tours_panel, name='tours_panel'),
    path('manager/users/', views.users_panel, name='users_panel'),
    path('manager/bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('manager/tours/edit/<int:tour_id>/', views.edit_tour, name='edit_tour'),
    path('manager/tours/delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),
    path('manager/tours/add/', views.add_tour, name='add_tour'),
    path('manager/users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('manager/users/add/', views.add_user, name='add_user'),
    path('user/bookings/', views.manage_bookings, name='manage_bookings'),
    path('tour/<int:tour_id>/review/', views.add_review, name='add_review'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('tour/<int:tour_id>/book/', views.create_booking, name='create_booking'),
    path('destinations/', views.tour_list, name='destination_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)