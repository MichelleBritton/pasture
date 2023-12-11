from .models import Booking
from .models import Menu
from django import forms


class DateInput(forms.DateInput):
    """
    Create a widget for date input
    """
    input_type = 'date'
    format = '%m/%d/%y'


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
    

class MenuForm(forms.ModelForm):
    """ 
    Create a form based on the Menu model so that
    staff can create a menu
    """


    class Meta:
        model = Menu
        fields = ('type', 'title', 'description', 'price',)