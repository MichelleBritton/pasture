from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    """
    Create a widget for date input
    """
    input_type = 'date'


class BookTableForm(forms.ModelForm):
    """
    Create a form based on the Booking model so that 
    users can make a reservation
    """

    class Meta:
        model = Booking
        exclude = ('username', )
        widgets = {
            'date': DateInput(),
        }
    
    