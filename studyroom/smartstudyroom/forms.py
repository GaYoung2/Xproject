from django import forms
from .models import Room, Seat

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat 
        fields = ['seat_id', 'room']