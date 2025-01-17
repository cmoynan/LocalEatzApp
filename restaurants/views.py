from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Restaurant, Booking
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    """
    View for the home page showing a list of all restaurants.
    """
    restaurants = Restaurant.objects.all()  # Get all restaurant objects
    return render(request, 'home.html', {'restaurants': restaurants})


@login_required
def book_table(request, restaurant_id=None, booking_id=None):
    """
    View to handle booking a table. Can handle
    both new bookings and editing existing ones.
    """
    restaurant = None
    if restaurant_id:
        # Fetch the restaurant by ID if provided
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if booking_id:
        # Fetch existing booking by ID if provided and
        # ensure it's by the current user
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        if restaurant is None:
            # Set the restaurant from the booking if it was not provided
            restaurant = booking.restaurant
    else:
        # Initialize an empty booking instance for new bookings
        booking = None

    if request.method == 'POST':
        # Handle form submission
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.restaurant = restaurant
            new_booking.user = request.user
            new_booking.save()

            # Send booking confirmation email
            subject = 'Booking Confirmation'
            html_message = render_to_string(
             'emails/booking_confirmation.html',
             {'user': request.user, 'booking': new_booking}
            )

            plain_message = strip_tags(html_message)
            send_mail(
             subject, plain_message, settings.DEFAULT_FROM_EMAIL,
             [request.user.email], html_message=html_message
            )

            if booking and booking.id != new_booking.id:
                # Delete the old booking if it was updated
                booking.delete()

            # Redirect to the user's bookings page
            return redirect('my_bookings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Initialize the form with existing booking data if in edit mode
        form = BookingForm(instance=booking)

    return render(request, 'restaurants/book_table.html', {
        'form': form,
        'restaurant': restaurant,
        'edit_mode': bool(booking)  # Indicates if the form is in edit mode
    })


def booking_success(request):
    """
    View to display a booking success message.
    """
    return render(request, 'restaurants/booking_success.html')


@login_required
def my_bookings(request):
    """
    View to list all bookings for the current user.
    """
    user = request.user
    # Filter bookings by the current user
    bookings = Booking.objects.filter(user=user)
    return render(request, 'users/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    """
    View to cancel a booking for the current user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    # Store the booking details before deletion
    booking_details = {
        'user': request.user,
        'booking': booking
    }

    # Delete the booking
    booking.delete()

    # Send booking cancellation email
    subject = 'Booking Cancellation'
    html_message = render_to_string(
        'emails/booking_cancellation.html', booking_details
     )

    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL,
              [request.user.email], html_message=html_message)

    return redirect('my_bookings')


@login_required
def edit_booking(request, booking_id):
    """
    View to edit an existing booking for the current user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Handle form submission for editing
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save()  # Save the booking
            messages.success(request, 'Booking updated successfully.')

            # Send booking update email
            subject = 'Booking Updated'
            html_message = render_to_string(
             'emails/booking_update.html',
             {'user': request.user, 'booking': updated_booking}

            )

            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL,
                      [request.user.email],
                      html_message=html_message)
            # Redirect to the user's bookings page
            return redirect('my_bookings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Initialize the form with existing booking data
        form = BookingForm(instance=booking)

    return render(request, 'restaurants/edit_booking.html', {
        'form': form,
        'restaurant': booking.restaurant,  # Pass the associated restaurant
        'booking': booking  # Pass the booking object being edited
    })
