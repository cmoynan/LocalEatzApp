from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'date', 'time', 'party_size']

def clean_time(self):
        time = self.cleaned_data['time']
        if time.minute not in [0, 30]:
            raise ValidationError('Time must be in half-hour increments (e.g., 12:00, 12:30).')
        return time