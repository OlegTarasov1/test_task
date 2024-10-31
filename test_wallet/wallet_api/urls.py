from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/wallets/<str:WALLET_UUID>/operation/', views.WalletOperation.as_view(), name = 'balance_manip'),
    path('api/v1/wallets/<str:WALLET_UUID>/', views.RetrieveWallet.as_view(), name = 'balance_get')

]