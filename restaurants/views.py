from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Restaurant, Booking


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            if form.is_valid():
            # Check if the restaurant is overbooked
             date = form.cleaned_data['date']
             time = form.cleaned_data['time']
             party_size = form.cleaned_data['party_size']
             existing_bookings = Booking.objects.filter(restaurant=restaurant, date=date, time=time).count()
            if existing_bookings >= restaurant.max_tables:
                messages.error(request, 'Sorry, no tables available at this time. Please choose a different time.')
            else:
                booking = form.save(commit=False)
                booking.restaurant = restaurant
                booking.save()
                return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'restaurants/book_table.html', {'form': form, 'restaurant': restaurant})

def booking_success(request):
    return render(request, 'restaurants/booking_success.html')      


