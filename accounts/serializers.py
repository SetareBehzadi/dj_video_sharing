from rest_framework import serializers
from accounts.models import Account
from playlist.models import Playlist


class AccountSerializer(serializers.ModelSerializer):
    subscription_count = serializers.SerializerMethodField()
    playlist_count = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ['id', 'username', 'email',  'playlist_count', 'subscription_count']

    def get_subscription_count(self, obj):
        return obj.user_subscriptions.count()
    
    def get_playlist_count(self, obj):
        return obj.playlists.count()

    def get_payment_count(self, obj):
        return obj.channel_payments.count()