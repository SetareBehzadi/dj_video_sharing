from django.contrib import admin

from playlist.models import Playlist


# Register your models here.
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title','owner')