from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("accounts/", include("allauth.urls")),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('book_table/<int:restaurant_id>/', views.book_table, name='book_table'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]


