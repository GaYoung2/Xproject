from django.contrib import admin
from .models import Room, Seat
from accounts.models import Account

class SeatInline(admin.TabularInline):
    model = Seat
    
@admin.register(Room)
class roomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [SeatInline]

class AccountAdmin(admin.ModelAdmin):
    list_display = ('student_num', 'username', 'password')

admin.site.register(Account, AccountAdmin)