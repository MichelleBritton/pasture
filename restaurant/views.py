from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookTableForm
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib import messages


def home(request):
    """
    Render Home page
    """
    return render(request, 'index.html')


def book(request):
    """
    Render Book page and display booking form
    """
    if request.method == 'POST':
        booking_form = BookTableForm(data=request.POST)        

        if booking_form.is_valid():
            instance = booking_form.save(commit=False)
            instance.username = User.objects.get(id=request.user.id)
            instance.email = request.user.email
            instance.save()
            messages.success(request,
                'Thank you, your reservation has been made')
            # return HttpResponseRedirect(reverse('my_profile'))
        else:
            messages.error(request, 'Sorry, the date and time you have requested has already been booked, please select another date or time')
            booking_form = BookTableForm()

    return render(
        request,
        'book.html',
        {
            "booking_form": BookTableForm()
        },
    )


def my_profile(request):
    """
    Render My Profile page to display user bookings
    """   
    # Filter bookings made by the user 
    bookings = Booking.objects.filter(username=request.user)
    context = {
        'bookings' : bookings,
    }
    return render(request, 'my_profile.html', context)


def edit_booking(request, booking_id):
    """ 
    Render Edit Booking page
    """
    # Get a copy of the reservation from the database
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookTableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request,
                'Thank you, your reservation has been changed')
            return redirect('my_profile')
        else:
            messages.error(request, 'Sorry, the date and time you have requested has already been booked, please select another date or time')
            form = BookTableForm()

    # Create an instance of the booking form and return it to the template in the context 
    # to pre-populate the form with current reservation details
    form = BookTableForm(instance=booking)
    context = {
        'form' : form
    }

    return render(request, "edit_booking.html", context)
