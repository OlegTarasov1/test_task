from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Wallet

class BalanceSerializer(serializers.ModelSerializer):
    wallet_uuid = serializers.CharField(read_only = True, max_length = 150)
    balance = serializers.IntegerField(read_only = True)
    amount = serializers.IntegerField(write_only = True)
    operationType = serializers.CharField(write_only = True, max_length = 150)

    
    def create(self, validated_data):
        wallet_uuid = self.context['request'].parser_context['kwargs'].get('WALLET_UUID')
        operation_type = validated_data['operationType']
        
        transfer = int(validated_data['amount'])
        if transfer < 0:
            raise ValidationError({"error": "You can't operate negative numbers"})
        try:
            wallet_obj = Wallet.objects.get(wallet_uuid = wallet_uuid) 
        except:
            raise ValidationError({'error': 'there was no such wallet_uuid found'})
        
        if wallet_obj.balance < transfer:
            raise ValidationError({'error': 'Not Enough Money'})
        elif operation_type == 'DEPOSIT':
            wallet_obj.balance += transfer
        elif operation_type == 'WITHDRAW':
            wallet_obj.balance -= transfer
        else:
            raise ValidationError({"error": "incorrect operation type was passed"})

        wallet_obj.save()
        return wallet_obj


    class Meta:
        model = Wallet
        fields = ['wallet_uuid', 'balance', 'amount', 'operationType']


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['wallet_uuid', 'balance']

