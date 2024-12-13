from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('about-us/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('admin/bookings/', views.bookings_panel, name='bookings_panel'),
    path('admin/tours/', views.tours_panel, name='tours_panel'),
    path('admin/users/', views.users_panel, name='users_panel'),
    path('admin/bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('admin/tours/edit/<int:tour_id>/', views.edit_tour, name='edit_tour'),
    path('admin/tours/delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),
    path('admin/tours/add/', views.add_tour, name='add_tour'),
    path('admin/users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('admin/users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/users/add/', views.add_user, name='add_user'),
    path('user/bookings/', views.manage_bookings, name='manage_bookings'),
    path('tour/<int:tour_id>/review/', views.add_review, name='add_review'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('tour/<int:tour_id>/book/', views.create_booking, name='create_booking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
