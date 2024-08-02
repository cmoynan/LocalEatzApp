from django.urls import path, include
from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),
    # Route for the home page, handled by the home view

    path(
        'accounts/',
        include('allauth.urls')
    ),
    # Route for account management handled by allauth
    # (e.g., login, signup, etc.)

    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),
    # Route to list all bookings for the logged-in user,
    # handled by the my_bookings view

    path(
        'book_table/<int:restaurant_id>/',
        views.book_table,
        name='book_table'
    ),
    # Route to book a table
    # at a specific restaurant,
    # handled by the book_table view

    path(
        'edit-booking/<int:booking_id>/',
        views.edit_booking,
        name='edit_booking'
    ),
    # Route to edit an existing booking, handled by the edit_booking view

    path(
        'booking_success/',
        views.booking_success,
        name='booking_success'
    ),
    # Route to display a booking success message,
    # handled by the booking_success view

    path(
        'cancel-booking/<int:booking_id>/',
        views.cancel_booking,
        name='cancel_booking'
    ),
    # Route to cancel a booking, handled by the cancel_booking view
]
