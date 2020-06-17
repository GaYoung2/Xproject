from django.contrib import admin
from .models import Room, Seat

class SeatInline(admin.TabularInline):
    model = Seat
    
@admin.register(Room)
class roomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [SeatInline]