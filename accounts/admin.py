from django.contrib import admin

from accounts.models import Account


@admin.register(Account)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('username', 'subscription_type','subscription_expiry')
