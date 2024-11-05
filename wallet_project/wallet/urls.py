from django.urls import path
from .views import dashboard, pay, request_money, transactions

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('pay/', pay, name='pay'),
    path('request-money/', request_money, name='request_money'),
    path('transactions/', transactions, name='transactions'),
]
