from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .models import Menu
from .forms import BookTableForm
from .forms import MenuForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from .filters import BookingFilter


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
            return redirect('my_profile')
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
            if request.user.is_staff:
                return redirect('manage_bookings')
            else:
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


def delete_booking(request, booking_id):
    """ 
    Render Delete Booking page and delete booking on confirmation
    """
    # Get a copy of the reservation from the database
    booking = get_object_or_404(Booking, id=booking_id)

    # If the user clicks on yes then delete the booking
    # Otherwise, return to My Profile
    if request.method == "POST":
        booking.delete()
        if request.user.is_staff:
            return redirect('manage_bookings')
        else:
            return redirect('my_profile')

    # If it is a GET request then render the delete confirmation page
    return render(request, "delete_booking.html")


def staff_profile(request):
    """
    Render Staff Profile page to display all bookings
    """   
    # Filter bookings for today's date
    today = datetime.today()
    bookings = Booking.objects.filter(date=today)

    context = {
        'bookings' : bookings,
    }
    return render(request, 'staff_profile.html', context)


def manage_bookings(request):
    """
    Render Manage Bookings page to display all bookings
    and ability to edit and delete them
    """   
    all_bookings = Booking.objects.order_by('date')
    booking_filter = BookingFilter(request.GET, queryset=all_bookings)
    all_bookings = booking_filter.qs

    context = {
        'all_bookings': all_bookings,
        "booking_filter": booking_filter,
    }
    return render(request, 'manage_bookings.html', context)


def menu(request):
    """
    Render Menu Page and retrieve Menu items from database
    """

    starters = Menu.objects.filter(type=1).values()
    mains = Menu.objects.filter(type=2).values()
    desserts = Menu.objects.filter(type=3).values()

    context = {
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
    }

    return render(request, 'menu.html', context)


def manage_menus(request):
    """
    Render Manage Menus Page and display  form
    """

    if request.method == 'POST':
        menu_form = MenuForm(data=request.POST)        

        if menu_form.is_valid():
            instance = menu_form.save(commit=False)            
            instance.save()
            messages.success(request,
                'Menu item has been created')
            return redirect('manage_menus')
        else:
            for error in menu_form.errors:
                messages.error(request, menu_form.errors[error])           
            menu_form = MenuForm()

    starters = Menu.objects.filter(type=1).values()
    mains = Menu.objects.filter(type=2).values()
    desserts = Menu.objects.filter(type=3).values()

    context = {
        "menu_form": MenuForm(),
        'starters': starters,
        'mains': mains,
        'desserts': desserts,
    }

    return render(request, 'manage_menus.html', context,)