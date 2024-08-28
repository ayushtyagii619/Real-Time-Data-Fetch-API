from rest_framework import serializers
from .models import TransactionDetail,AyushUser

from django_filters import rest_framework as filters

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = AyushUser
        fields = ['email','password']
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AyushUser
        fields = ['id','email','name']