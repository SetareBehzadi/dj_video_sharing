from django.db import models

from django.contrib.auth.models import User
from playlist.models import Playlist


class Subscription(models.Model):
    subscriber = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscriptions')
    channel = models.ManyToManyField(User, related_name='user_subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)




