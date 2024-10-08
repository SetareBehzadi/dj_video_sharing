from django.shortcuts import render
from rest_framework import generics, status

from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer


# Create your views here.
class PlayListView(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer