""" Basic models, such as user profile """
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class EthAccount(models.Model):
    account_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)
    account_address = models.CharField(max_length=300)
    account_password = models.CharField(max_length=300, default="password123456789")
    created_date= models.DateTimeField(default=timezone.now)
    balance = models.DecimalField(max_digits=100, decimal_places=18, default=0)

    def __str__(self):
        return self.account_address


class Transaction(models.Model):
    tx_id = models.AutoField(primary_key=True)
    tx_hash = models.CharField(max_length=300)
    account_address = models.ForeignKey(EthAccount, on_delete=models.CASCADE)
    tx_time = models.DateTimeField(default=timezone.now)
    deposit_amount = models.DecimalField(max_digits=100, decimal_places=18)
    withdrawal_amount = models.DecimalField(max_digits=100, decimal_places=18)
    withdrawal_address = models.CharField(max_length=300)

    def __str__(str):
        return self.tx_hash

