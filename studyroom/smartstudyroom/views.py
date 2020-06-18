from django.shortcuts import render
from .models import Room, Seat
from django.views import generic
from .forms import SeatForm

def index(request):
    num_books = Room.objects.all()
    context = {
        'room_list': num_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def study(request):
    context = {}
    return render(request, 'study.html', context)

def reserve(request):
    context = {}
    seat_num = SeatForm(request.POST)
    if form.is_valid():
        seat = Seat.objects.get(pk=form.cleaned_data.get('seat_id'))
        if seat.SIT_STATUS == 'a':
            seat.SIT_STATUS = 'u'
            seat.save()
        else:
            return HttpResponse('Not available seat!')
    return render(request, 'index.html', context)
