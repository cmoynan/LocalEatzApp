from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Restaurant, Booking


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

@login_required
def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking
            booking = form.save(commit=False)
            booking.restaurant = restaurant
            booking.save()
            
            messages.success(request, 'Your table has been successfully booked!')
            return redirect('booking_success')
        else:
            
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()

    return render(request, 'restaurants/book_table.html', {
        'form': form,
        'restaurant': restaurant
    })

def booking_success(request):
    return render(request, 'restaurants/booking_success.html')     


