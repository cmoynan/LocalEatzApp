from django.contrib import admin
from .models import Restaurant, Booking

# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'max_tables')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','restaurant', 'name', 'date', 'time', 'party_size')
    list_filter = ('restaurant', 'date')
    search_fields = ('name', 'restaurant__name')
