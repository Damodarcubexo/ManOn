from django.contrib import admin
from game.models import GameModel


# Register your models here.
class details(admin.ModelAdmin):
    list_display = ['id', "user"]


admin.site.register(GameModel, details)
