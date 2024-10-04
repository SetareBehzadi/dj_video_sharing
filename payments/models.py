from django.db import models

from subscriptions.models import Subscription
from django.contrib.auth.models import User



class Payment(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber_payments')
    channel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='channel_payments')
    fee = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
