from rest_framework import serializers

from playlist.models import Playlist


class PlaylistSerializer(serializers.Serializer):
    class Meta:
        model = Playlist
        fields = '__all__'
