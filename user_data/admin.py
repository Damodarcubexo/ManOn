from django.contrib import admin
from .models import UserTable


# Register your models here.
class username(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'player_id']




admin.site.register(UserTable, username)
