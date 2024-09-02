from django.urls import path
from .views import ListTransaction,UserLoginView,UserProfileView

urlpatterns = [
    path('transaction/',ListTransaction.as_view(),name='transactions'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
] 