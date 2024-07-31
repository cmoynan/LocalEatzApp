from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    max_tables = models.IntegerField(default=3)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking for {self.name} at {self.restaurant.name} on {self.date} at {self.time}"



 