from django.shortcuts import render


def home(request):

    return render(request, 'index.html')

def book(request):

    return render(request, 'book.html')
