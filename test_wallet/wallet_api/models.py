from django.db import models

class Wallet(models.Model):
    wallet_uuid = models.SlugField(max_length = 150, unique = True)
    balance = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['wallet_uuid'])
        ]