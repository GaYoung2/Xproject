from django.shortcuts import render
from .models import Room
from django.views import generic

def index(request):
    num_books = Room.objects.all()
    context = {
        'room_list': num_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)