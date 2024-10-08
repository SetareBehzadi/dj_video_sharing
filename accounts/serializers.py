from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    followerCount = serializers.IntegerField(default=10)
    class Meta:
        model = Account
        fields = '__all__'