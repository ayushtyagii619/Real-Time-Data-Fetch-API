from rest_framework import serializers
from .models import TransactionDetail,AyushUser

from django_filters import rest_framework as filters

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

class TransactionFilter(filters.FilterSet):
    txn_id = filters.CharFilter(field_name='txn_id', lookup_expr='icontains')
    pg_pay_mode = filters.CharFilter(field_name='pg_pay_mode', lookup_expr='icontains')
    status = filters.CharFilter(field_name='status')
    paid_start_date = filters.DateTimeFilter(field_name='settlement_date',lookup_expr='gte')
    paid_end_date = filters.DateTimeFilter(field_name='settlement_date',lookup_expr='lte')

    class Meta:
        model = TransactionDetail
        fields = ['txn_id','pg_pay_mode','status','paid_start_date','paid_end_date']

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = AyushUser
        fields = ['email','password']
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AyushUser
        fields = ['id','email','name']