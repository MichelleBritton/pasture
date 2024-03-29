"""pasture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('book/', views.book, name='book'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
    path('staff_profile/', views.staff_profile, name='staff_profile'),
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('menu/', views.menu, name='menu'),
    path('manage_menus/', views.manage_menus, name='manage_menus'),
    path('edit_menu/<menu_id>', views.edit_menu, name='edit_menu'),
    path('delete_menu/<menu_id>', views.delete_menu, name='delete_menu'),
]
