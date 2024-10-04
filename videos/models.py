from django.db import models

from playlist.models import Playlist


class Video(models.Model):
    title = models.CharField(max_length=250)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL,
                                 related_name='videos', blank=True, null=True)
    url = models.URLField()
    length = models.PositiveIntegerField()
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


