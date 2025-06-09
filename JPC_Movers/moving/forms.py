
from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    workers = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])
    hours = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])

    class Meta:
        model = Reservation
        fields = [
            'customer_name', 'customer_email', 'customer_phone',
            'move_date', 'origin_address', 'destination_address',
            'service', 'workers', 'hours'
        ]

class ReservationLookupForm(forms.Form):
    reservation_number = forms.UUIDField()