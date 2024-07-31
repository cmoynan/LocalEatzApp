from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

# Form for creating or updating bookings
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'party_size']
  