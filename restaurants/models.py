from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

# Model for storing information about restaurants


class Restaurant(models.Model):
    # Name of the restaurant
    name = models.CharField(max_length=255)
    # Address of the restaurant
    address = models.CharField(max_length=255)
    # Optional description of the restaurant
    description = models.TextField(blank=True)
    # Maximum number of tables available in the restaurant
    max_tables = models.IntegerField(default=3)

    def __str__(self):
        # Return the name of the restaurant as the string representation
        return self.name

# Model for storing booking details


class Booking(models.Model):
    # Reference to the user who made the booking
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Reference to the restaurant where the booking was made
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # Name of the person who made the booking
    name = models.CharField(max_length=100)
    date = models.DateField()  # Date of the booking
    time = models.TimeField()  # Time of the booking
    party_size = models.PositiveIntegerField()  # Number of people in the party

    def __str__(self):
        # String representation of the booking
        return (
            f"Booking for {self.name} at {self.restaurant.name} "
            f"on {self.date} at {self.time}")
