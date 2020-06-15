from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('student_num', 'username', 'password')

admin.site.register(Account, AccountAdmin)