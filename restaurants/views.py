from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Restaurant, Booking
from django.contrib import messages


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

@login_required
def book_table(request, restaurant_id=None, booking_id=None):
    restaurant = None
    if restaurant_id:
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if booking_id:
        # Fetch existing booking
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        if restaurant is None:
            restaurant = booking.restaurant
    else:
        # For new bookings
        booking = None

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.restaurant = restaurant
            new_booking.user = request.user
            new_booking.save()

            if booking and booking.id != new_booking.id:
                # Delete the old booking if updating
                booking.delete()

            return redirect('my_bookings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'restaurants/book_table.html', {
        'form': form,
        'restaurant': restaurant,
        'edit_mode': bool(booking)
    })

def booking_success(request):
    return render(request, 'restaurants/booking_success.html')

def my_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)  # Filter by user
    return render(request, 'users/my_bookings.html', {'bookings': bookings})     

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()  # Remove the booking
    return redirect('my_bookings')

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('my_bookings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'restaurants/edit_booking.html', {
        'form': form,
        'restaurant': booking.restaurant,
        'booking': booking
    })


