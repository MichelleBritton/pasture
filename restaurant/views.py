from django.shortcuts import render
from .models import Booking
from .forms import BookTableForm
from django.contrib.auth.models import User


def home(request):

    return render(request, 'index.html')

def book(request):

    if request.method == 'POST':
        booking_form = BookTableForm(data=request.POST)

        if booking_form.is_valid():
            instance = booking_form.save(commit=False)
            instance.username = User.objects.get(id=request.user.id)
            instance.email = request.user.email
            instance.save()
        else:
            booking_form = BookTableForm()

    return render(
        request,
        'book.html',
        {
            "booking_form": BookTableForm()
        },
    )
