from django.contrib import admin
from .models import Booking
from.models import Menu


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('username', 'name', 'phone_no', 'date', 'time', 'no_of_guests')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    list_display = ('type', 'title', 'description', 'price')