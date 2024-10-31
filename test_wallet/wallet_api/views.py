from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound
from .models import Wallet
from .serializers import BalanceSerializer, WalletSerializer

class WalletOperation(CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = BalanceSerializer


class RetrieveWallet(RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_object(self):
        wallet_uuid = self.kwargs.get('WALLET_UUID')
        try:
            return Wallet.objects.get(wallet_uuid = wallet_uuid)
        except:
            raise NotFound(detail = 'No wallet was found')

