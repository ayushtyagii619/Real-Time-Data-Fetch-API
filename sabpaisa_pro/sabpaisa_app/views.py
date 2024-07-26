from rest_framework.decorators import api_view,permission_classes
from .serializers import TransactionSerializer,UserLoginSerializer,UserProfileSerializer,TransactionFilter
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import TransactionDetail
from rest_framework.response import Response
from django.shortcuts import render

#@api_view(['GET','POST'])
#@permission_classes([AllowAny])
class ListTransaction(APIView):
    def post(self,request,id=0):
            paid_start_date = request.data.get('paid_start_date')
            paid_end_date = request.data.get('paid_end_date')
            if paid_start_date and paid_end_date:
                if paid_start_date > paid_end_date:
                        return Response(
                        {'msg': 'Start date cannot be greater than end date.'},status=status.HTTP_404_NOT_FOUND
                )
            filterset = TransactionFilter(request.data, queryset=TransactionDetail.objects.all())
            if filterset.is_valid():
                 filtered_transaction = filterset.qs
            else:
                 filtered_transaction = TransactionDetail.objects.all()
            serializer = TransactionSerializer(filtered_transaction, many=True)
            return Response(serializer.data)
    
def login_page(request):
    return render(request, 'login.html')


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
