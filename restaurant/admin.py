from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('username', 'name', 'phone_no', 'date', 'time', 'no_of_guests')