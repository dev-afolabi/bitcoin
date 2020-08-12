from django.db import models
from transactions.models import User
# Create your models here.

class BankTransfer(models.Model):
    name = models.CharField( max_length=50)
    bank_name = models.CharField( max_length=50)
    account_number = models.CharField( max_length=50)

    def __str__(self):
        return str(self.name)

class BTCTransfer(models.Model):
    name = models.CharField( max_length=50)
    btc_address = models.CharField( max_length=50)

    def __str__(self):
        return str(self.name)

class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
