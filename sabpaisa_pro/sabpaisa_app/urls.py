from django.urls import path
from .views import ListTransaction,UserLoginView,UserProfileView,login_page

urlpatterns = [
    path('',login_page,name='login_page'),
    path('transaction/',ListTransaction.as_view(),name='home'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
]