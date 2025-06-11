
from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'move_datetime',
            'origin_address',
            'destination_address',
            'service',
            'workers',
            'hours'
        ]
        widgets = {
            'move_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'workers': forms.Select(),
            'hours': forms.Select(),
        }


class ReservationLookupForm(forms.Form):
    reservation_number = forms.UUIDField()