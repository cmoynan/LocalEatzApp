from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import BookingForm

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'book_table.html', {'restaurant': restaurant})

def submit_booking(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.restaurant = restaurant
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'restaurants/booking_form.html', {'form': form, 'restaurant': restaurant})