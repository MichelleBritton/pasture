from .models import Booking
from django import forms


class BookTableForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('phone_no', 'date', 'time', 'no_of_guests', 'notes',)
    
    