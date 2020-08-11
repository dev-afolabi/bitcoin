from django.db import models
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
