from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """
    Model to store data regarding booking reservations
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking"
    )
    phone_no = models.CharField(max_length=11, default=0)
    date = models.DateField()
    time = models.IntegerField()
    no_of_guests = models.IntegerField()
    notes = models.TextField()


