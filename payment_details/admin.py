from django.contrib import admin
from .models import BTCTransfer, BankTransfer

# Register your models here.
admin.site.register(BTCTransfer)
admin.site.register(BankTransfer)

