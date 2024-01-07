from django.db import models
from user.models import UserBankAccount
# Create your models here.

DEPOSIT = 1

TRANSACTION_TYPE = (
    (DEPOSIT, 'Deposit'),
)
class Transaction(models.Model):

    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places = 2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places = 2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['timestamp']