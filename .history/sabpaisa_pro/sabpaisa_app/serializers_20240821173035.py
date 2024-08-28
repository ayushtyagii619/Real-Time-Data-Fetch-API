from rest_framework import serializers
from .models import TransactionDetail,AyushNewUser

from django_filters import rest_framework as filters

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = AyushNewUser
        fields = ['email','password']
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AyushNewUser
        fields = ['id','email','name']