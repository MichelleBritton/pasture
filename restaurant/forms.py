from .models import Booking
from .models import Menu
from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    """
    Create a widget for date input
    """
    input_type = 'date'
    format = '%d/%m/%y'


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

    def clean(self):
        """
        Get form data and clean to ensure reservations cannot be 
        made in the past
        """
        date = self.cleaned_data['date']

        # Throw validation errors if date is in the past
        if date < datetime.today().date():
            raise ValidationError(
                'Invalid date - Reservation cannot be made in the past'
            )


class MenuForm(forms.ModelForm):
    """
    Create a form based on the Menu model so that
    staff can create a menu
    """

    class Meta:
        model = Menu
        fields = ('type', 'title', 'description', 'price',)
