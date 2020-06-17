from django.db import models
from django.contrib.auth.models import User
import uuid 
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    row = models.IntegerField(null=True)
    column = models.IntegerField(null=True)

    #language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    #genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

class Seat(models.Model):
    seat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    #seat_num = models.IntegerField(null=True)
    missed_time = models.FloatField(null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    #present_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    SIT_STATUS = (
        ('u', 'Use'),
        ('m', 'Missed'),
        ('a', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=SIT_STATUS,
        blank=True,
        default='a',
        help_text='Present Sit Status',
    )