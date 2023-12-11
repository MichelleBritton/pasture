from django.db import models
from django.contrib.auth.models import User


# List of times available to book when making a reservation
TIMES = (
    (1, '12:00-13:50'),
    (2, '14:00-15:50'),
    (3, '16:00-17:50'),
    (4, '18:00-19:50'),
    (5, '20:00-21:50')
)


TYPES = (
    (1, 'Starter'),
    (2, 'Main'),
    (3, 'Dessert'),
    (4, 'Side'),
    (5, 'Sauce'),
)


class Booking(models.Model):
    """
    Model to store data regarding booking reservations
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking"
    )
    name = models.CharField(max_length=80)
    phone_no = models.CharField(max_length=11, default=0)
    date = models.DateField()
    time = models.IntegerField(choices=TIMES, default=1)
    no_of_guests = models.IntegerField(default=1)
    notes = models.TextField(blank=True)


    class Meta:
        """
        Ensure that the table cannot be double booked
        """
        constraints = [
            models.UniqueConstraint(fields=['date', 'time'], name='unique_booking'),
        ]


class Menu(models.Model):
    """ 
    Model to store data regarding menu items
    """
    type = models.IntegerField(choices=TYPES)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.FloatField()

