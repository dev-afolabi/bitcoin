from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from transactions.models import Deposit, Withdrawal
from payment_details.models import Notification, Message

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
        messages = Message.objects.filter(user=user)
        messages_count = Message.objects.filter(user=user).count()

        context = {
                    "user": user,
                    "deposit": deposit,
                    "withdrawal": withdrawal,
                    "notifications":notifications,
                    "messagess":messages,
                    "messages_count":messages_count
                  }

        return render(request, "dashboard/dashboard.html", context)

@login_required
def inbox(request):
    if not request.user.is_authenticated:
        return render(request, "registration/login.html", {})
    else:
        user = request.user
        messages = Message.objects.filter(user=user)
        messages_count = Message.objects.filter(user=user).count()
        
        context = {
                    "messages":messages,
                    "messages_count":messages_count
                  }
        return render(request, 'dashboard/inbox.html', context)

@login_required
def read_mail(request, pk):
    return render(request, 'dashboard/read.html', {'message':get_object_or_404(Message, pk=pk)})

@login_required
def compose(request):
    return render(request, 'dashboard/compose.html')