from django.db import models
from django.contrib.auth.models import User
import uuid 
from django.urls import reverse
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    row = models.IntegerField(null=True)
    column = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])


    #language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    #genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

class Seat(models.Model):
    seat_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    seat_num = models.IntegerField(null=True)
    reserved_time = models.TimeField(null=True,blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    SEAT_STATUS = (
        ('u', 'Use'),
        ('r', 'Reserve'),
        ('a', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=SEAT_STATUS,
        blank=True,
        default='a',
        help_text='Present Sit Status',
    )