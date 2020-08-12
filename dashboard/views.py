from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import Deposit, Withdrawal
from payment_details.models import Notification

# Create your views here.
@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, "registration/login.html", {})
    else:
        user = request.user
        deposit = Deposit.objects.filter(user=user)
        # deposit_sum = deposit.aggregate(Sum('amount'))['amount__sum']
        withdrawal = Withdrawal.objects.filter(user=user)
        # withdrawal_sum = withdrawal.aggregate(Sum('amount'))['amount__sum']
        notifications = Notification.objects.filter(user=user)

        context = {
                    "user": user,
                    "deposit": deposit,
                    "withdrawal": withdrawal,
                    "notifications":notifications
                  }

        return render(request, "dashboard/dashboard.html", context)