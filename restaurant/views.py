from django.shortcuts import render
from .models import Booking
from .forms import BookTableForm


def home(request):

    return render(request, 'index.html')

def book(request):

    booking_form = BookTableForm(data=request.POST, instance=request.user)
    
    if booking_form.is_valid():    
        booking_form.instance.username = request.user.username    
        booking = booking_form.save(commit=False)
        booking.save()
    else:
        booking_form = BookTableForm()

    return render(
        request,
        'book.html',
        {
            "booking_form": BookTableForm()
        },
    )
