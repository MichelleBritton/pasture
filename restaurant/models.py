from django.db import models
from django.contrib.auth.models import User


# List of times available to book when making a reservation
TIMES = (
    (1, '12:00 - 13:50'),
    (2, '14:00 - 15:50'),
    (3, '16:00 - 17:50'),
    (4, '18:00 - 19:50'),
    (5, '20:00 - 21:50')
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
    no_of_guests = models.IntegerField()
    notes = models.TextField(blank=True)


