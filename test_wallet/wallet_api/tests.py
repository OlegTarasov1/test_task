from rest_framework.test import APITestCase
from rest_framework import status
from .models import Wallet
from django.urls import reverse

class TestWallet(APITestCase):

    def test_get_check(self):
        url_get = reverse('balance_get', kwargs = {'WALLET_UUID': 'test_for_get'})
        test_obj = Wallet.objects.create(wallet_uuid = 'test_for_get', balance = 100) 
        response = self.client.get(url_get)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        

    def test_post_check(self):
        test_object = Wallet.objects.create(wallet_uuid = 'some_uuid', balance = 10000)
        url_post = reverse('balance_manip', kwargs = {'WALLET_UUID': 'some_uuid'})

        # invalid operation type:
        data = {
            'operationType': 'invalid',
            'amount': 100
        }

        response = self.client.post(url_post, data, format = 'json')
        response = response.data.get('error')
        self.assertEqual(response, 'incorrect operation type was passed')

        # no such wallet_uuid
        data = {
            'operationType': 'DEPOSIT',
            'amount': 100
        }
        temp_url_post = reverse('balance_manip', kwargs = {'WALLET_UUID': 'some_notexisting_uuid'})
        response = self.client.post(temp_url_post, data, format = 'json')
        response = response.data.get('error')
        self.assertEqual(response, 'there was no such wallet_uuid found')

        # not enogh money
        temp_data = {
            'operationType': 'WITHDRAW',
            'amount': 9999999
        }
        response = self.client.post(url_post, temp_data, format = 'json')
        response = response.data.get('error')
        self.assertEqual(response, 'Not Enough Money')

        # negative number passed
        temp_data = {
            'operationType': 'WITHDRAW',
            'amount': -1
        }
        response = self.client.post(url_post, temp_data, format = 'json')
        response = response.data.get('error')
        self.assertEqual(response, "You can't operate negative numbers")

        # all fine
        response = self.client.post(url_post, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # weghed testing
        for i in range(1000):
            response = self.client.post(url_post, data, format = 'json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)