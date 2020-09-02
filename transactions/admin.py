from django.contrib import admin

from .models import Deposit, Withdrawal
# Register your models here.
class DepositAdmin(admin.ModelAdmin): 
    list_display = ('user', 'amount', 'status', 'timestamp')
  


admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdrawal)