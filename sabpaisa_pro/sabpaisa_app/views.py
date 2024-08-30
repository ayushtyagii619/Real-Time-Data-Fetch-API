from rest_framework.decorators import api_view,permission_classes
from .serializers import TransactionSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import TransactionDetail
from rest_framework.response import Response
from django.shortcuts import render
from django_filters import rest_framework as filters

#@api_view(['GET','POST'])
#@permission_classes([AllowAny])

class TransactionFilter(filters.FilterSet):
    txn_id = filters.CharFilter(field_name='txn_id', lookup_expr='icontains')
    pg_pay_mode = filters.CharFilter(field_name='pg_pay_mode', lookup_expr='icontains')
    status = filters.CharFilter(field_name='status')
    paid_start_date = filters.DateTimeFilter(field_name='settlement_date',lookup_expr='gte')
    paid_end_date = filters.DateTimeFilter(field_name='settlement_date',lookup_expr='lte')

    class Meta:
        model = TransactionDetail
        fields = ['txn_id','pg_pay_mode','status','paid_start_date','paid_end_date']    


class ListTransaction(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id=0):
            paid_start_date = request.data.get('paid_start_date')
            paid_end_date = request.data.get('paid_end_date')
            report_status = request.data.get('report_status')
            if paid_start_date and paid_end_date:
                if paid_start_date > paid_end_date:
                        return Response(
                        {'Start date cannot be greater than end date.'},status=status.HTTP_404_NOT_FOUND
                )
            if report_status:
                allowed_report_types = ["SUCCESS", "FAILED"]
                if report_status not in allowed_report_types:
                    return Response({"message": f'{report_status} is not a valid report type'}, status=status.HTTP_400_BAD_REQUEST)
                request.data['status'] = report_status

            filterset = TransactionFilter(request.data, queryset=TransactionDetail.objects.all())
            if not filterset.is_valid():
                return Response(filterset.errors,status=status.HTTP_404_NOT_FOUND)
            filtered_transaction = filterset.qs

            if not filtered_transaction.exists():
                return Response(
                    {'No transactions found matching the provided filters.'}, 
                    status=status.HTTP_404_NOT_FOUND
            )
        
            serializer = TransactionSerializer(filtered_transaction,many=True)
            return Response(serializer.data)

            


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token),
    

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                access_token, refresh_token = get_tokens_for_user(user)
                return Response({'access_token':access_token, 'refresh_token': refresh_token, 'msg':'Login Successful'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    def get(self,request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
