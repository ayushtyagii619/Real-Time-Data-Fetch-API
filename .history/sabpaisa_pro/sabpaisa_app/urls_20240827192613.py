from django.urls import path
from .views import ListTransaction,UserLoginView,UserProfileView,login_page,home_page

urlpatterns = [
    path('',login_page,name='login_page'),
    path('home/',home_page,name='home'),
    path('home/transaction/',ListTransaction.as_view(),name='transactions'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
] 