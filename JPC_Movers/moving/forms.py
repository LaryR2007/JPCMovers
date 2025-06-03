
from .models import Service, Reservation
from django import forms


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_email', 'customer_phone', 'move_date', 'origin_address', 'destination_address']

class ReservationLookupForm(forms.Form):
    reservation_number = forms.UUIDField()