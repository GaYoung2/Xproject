from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:pk>', views.room_detail_view, name='room-detail'),
    path('room/<int:pk>/reservation', views.room_seats_reservation, name='room-seats-reservation'),
]