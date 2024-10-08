from rest_framework import serializers

from playlist.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    video_count = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = '__all__'

    def get_video_count(self, obj):
        return obj.videos.count()
