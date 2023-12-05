import django_filters
from .models import Booking
from django import forms


class BookingFilter(django_filters.FilterSet):
    """ 
    Filter bookings by name or date
    """

    name = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter(
        lookup_expr='icontains',
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'data-provide': 'datepicker',
                'type': 'date',
            }
        )
    )

    class Meta: 
        model = Booking
        fields = ['name', 'date']
        