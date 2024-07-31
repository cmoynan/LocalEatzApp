from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

# Model for storing information about restaurants
class Restaurant(models.Model):
    name = models.CharField(max_length=255)  # Name of the restaurant
    address = models.CharField(max_length=255)  # Address of the restaurant
    description = models.TextField(blank=True)  # Optional description of the restaurant
    max_tables = models.IntegerField(default=3)  # Maximum number of tables available in the restaurant

    def __str__(self):
        return self.name  # Return the name of the restaurant as the string representation

# Model for storing booking details
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Reference to the user who made the booking
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Reference to the restaurant where the booking was made
    name = models.CharField(max_length=100)  # Name of the person who made the booking
    date = models.DateField()  # Date of the booking
    time = models.TimeField()  # Time of the booking
    party_size = models.PositiveIntegerField()  # Number of people in the party

    def __str__(self):
        return f"Booking for {self.name} at {self.restaurant.name} on {self.date} at {self.time}"  # String representation of the booking
