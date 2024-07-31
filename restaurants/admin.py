from django.contrib import admin
from .models import Restaurant, Booking

# Register your models here.

# Register the Restaurant model with the Django admin
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'max_tables')

# Register the Booking model with the Django admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','restaurant', 'name', 'date', 'time', 'party_size')
    list_filter = ('restaurant', 'date')
    search_fields = ('name', 'restaurant__name')
