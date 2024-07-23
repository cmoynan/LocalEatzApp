from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import BookingForm

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.restaurant = restaurant
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'restaurants/book_table.html', {'form': form, 'restaurant': restaurant})

def booking_success(request):
    return render(request, 'restaurants/booking_success.html')      


