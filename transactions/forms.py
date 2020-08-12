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
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES, required=True, widget=forms.RadioSelect())
    class Meta:
        model = Withdrawal
        fields = ["amount","payment_option","bank_name","account_number","IBAN_number","swift_code","wallet_address"]

        widgets = {
            'amount' : forms.TextInput(attrs={'class': 'form-control'}),
            'payment_option' : RadioSelect(attrs={'class': 'form-control'}),
            'bank_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'account_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'IBAN_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'swift_code' : forms.TextInput(attrs={'class': 'form-control'}),
            'wallet_address' : forms.TextInput(attrs={'class': 'form-control'}),
        }

