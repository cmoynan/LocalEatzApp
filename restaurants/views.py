from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Restaurant

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})

def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'book_table.html', {'restaurant': restaurant})

def submit_booking(request, restaurant_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        party_size = request.POST.get('party_size')
        
        
        return HttpResponse("Booking submitted successfully!")
    return redirect('home')  