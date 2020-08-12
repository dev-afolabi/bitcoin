from django.contrib import admin
from .models import BTCTransfer, BankTransfer, Notification

# Register your models here.
admin.site.register(BTCTransfer)
admin.site.register(BankTransfer)
# admin.site.register(Notification)

