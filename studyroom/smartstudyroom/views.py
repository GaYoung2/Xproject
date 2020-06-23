from django.shortcuts import render,get_object_or_404
from .models import Room, Seat
from django.views import generic
from .forms import SeatForm
from .comm import transmit
import json
from django.utils import timezone

def index(request):
    num_books = Room.objects.all()
    context = {
        'room_list': num_books,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def room_detail_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    seat_list = []
    status_list = []
    data = transmit(room.ip)
    for i in range(1,7):
        seat_obj = Seat.objects.get(room=room, seat_num=i)
        seat_list.append((seat_obj.seat_num))
        if data[i-1]=='0'and seat_obj.status!='r':
            status_list.append(0)
            seat_obj.status='a'
        else:
            status_list.append(1)
            if seat_obj.status=='r':
                seat_obj.reserved_time=None;
            seat_obj.status='u'
        seat_obj.save()
        print(seat_obj.status)
    return render(request, 'smartstudyroom/room_detail.html', context={'room':room,'seat_list':seat_list, 'pk':pk,'status':status_list})

def room_seats_reservation(request, pk):
    seat_list = []
    status_list = []
    seat = request.GET.get('seat', None)  # seat 번호 ex) 1, 2, 3
    room = get_object_or_404(Room, pk=pk)
    seat_obj = Seat.objects.get(seat_num=seat)
    seat_obj.status = 'r'
    seat_obj.reserved_time = timezone.now()
    seat_obj.save()
    for i in range(1,room.row*room.column+1):
        seat_obj = Seat.objects.get(room=room, seat_num=i)
        seat_list.append((seat_obj.seat_num))
        if i == int(seat):
            status_list.append(2)
        elif seat_obj.status=='a':
            status_list.append(0)
        else:
            status_list.append(1)
    print(status_list)
    return render(request, 'smartstudyroom/room_status.html', context={'room':room,'seat_list':seat_list, 'pk':pk,'status':status_list})
