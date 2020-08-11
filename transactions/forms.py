from django import forms
from django.forms.widgets import Select, RadioSelect

from .models import Deposit, Withdrawal

PAYMENT_CHOICES = [
    ("Bank Transfer", "Bank Transfer"),
    ("Bitcoin Transfer", "Bitcoin Payment"),
]

class DepositForm(forms.ModelForm):
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES, required=True, widget=forms.RadioSelect())
    class Meta:
        model = Deposit
        fields = ["amount", "payment_option"]

        widgets = {
            'amount' : Select(attrs={'class': 'form-control'}),
            'payment_option' : RadioSelect(attrs={'class': 'controls'}),
        }



class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ["bank_name","account_number","IBAN_number","amount","swift_code"]

