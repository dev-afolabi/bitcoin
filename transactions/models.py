from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django import forms

# Create your models here.
User = settings.AUTH_USER_MODEL

AMOUNT_CHOICES = (
    ("$500", "$500"),
    ("$750", "$750"),
    ("$1000", "$1000"),
    ("$1,500", "$1,500"),
    ("$2,000", "$2,000"),
    ("$3,000", "$3,000"),
    ("$5,000", "$5,000"),
    ("$7,000", "$7000"),
    ("$10,000", "$10,000"),
    )

class Deposit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount= models.CharField(max_length=25, choices=AMOUNT_CHOICES,help_text="Select amount to deposit")
    payment_option = models.CharField(max_length=25,help_text="Select payment option")
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(
      decimal_places=2,
      max_digits=12,
      validators=[
          MinValueValidator(Decimal('10.00'))
          ]
      )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)