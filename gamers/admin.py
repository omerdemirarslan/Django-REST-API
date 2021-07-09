""" Gamers Model Admin Site Registrations """
from django.contrib import admin
from gamers.models import GameUser
from arena.helpers.helper import download_csv


# Register your models here.


class GameUserAdmin(admin.ModelAdmin):
    """
    To Customize Admin Model
    """
    list_display = ('full_name', 'username', 'email', 'is_active', 'birthdate', 'about')
    search_fields = ('user__first_name', 'user__last_name', 'user__username', 'user__email',
                     'user__is_active', 'birthdate')
    list_filter = ('user', 'user__is_active')
    actions = [download_csv]


admin.site.register(GameUser, GameUserAdmin)

admin.site.site_header = "Gamer Arena Admin"
admin.site.site_title = "Gamer Arena Admin"
admin.site.index_title = "Welcome to Gamer Arena"
