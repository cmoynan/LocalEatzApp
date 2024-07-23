
from django.shortcuts import render
from .models import Restaurant

# Create your views here.


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})
