from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import DepositForm, WithdrawalForm
# from formtools.wizard.views import SessionWizardView
from .models import Withdrawal,User,Deposit
from payment_details.models import BTCTransfer, BankTransfer, Notification


withdrawal_message = "your withdrawal is being proccessed"
deposit_message = "you made a deposit request"


@login_required()
def deposit_view(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        notifications = Notification.objects.filter(user=request.user)
        title = "Deposit"
        form = DepositForm(request.POST or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user

            # adds users deposit to balance.
            # deposit.user.balance += deposit.amount
            # deposit.user.save()
            deposit.save()
            Notification.objects.create(user=request.user, message=deposit_message)
            messages.success(request, 'Your deposit will be proccesed when funds have been posted'
                             .format(deposit.amount))
            if deposit.payment_option == "Bank Transfer":
                return redirect("bank-details")
            else:
                return redirect("bitcoin-details")

        context = {
                    "title": title,
                    "form": form,
                    "notifications":notifications
                  }
        return render(request, "transactions/deposit_form.html", context)


@login_required()
def withdrawal_view(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        notifications = Notification.objects.filter(user=request.user)
        title = "Withdraw"
        form = WithdrawalForm(request.POST or None)

        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            # checks if user is tring Withdraw more than his balance.
            if withdrawal.user.balance >= withdrawal.amount:
                # substracts users withdrawal from balance
                withdrawal.user.balance -= withdrawal.amount
                withdrawal.user.save()
                withdrawal.save()
                Notification.objects.create(user=request.user, message=withdrawal_message)
                messages.error(request, 'Your Withdrawal was successfull')
                return redirect("dashboard")

            else:
                messages.error(
                    request,
                    'You Cannot withdraw  More Than Your Balance.'
                    )
        context = {
                    "title": title,
                    "form": form,
                    "notifications":notifications
                    }
        return render(request, "transactions/withdrawal_form.html", context)

@login_required
def bank_payment_details(request):
    try:
        details = BankTransfer.objects.get(name='bank account')
    except ObjectDoesNotExist:
        pass
    return render(request, "transactions/bank_details.html", {'details':details})

@login_required
def bitcoin_payment_details(request):
    try:
        details = BTCTransfer.objects.get(name='bitcoin wallet')
    except ObjectDoesNotExist:
        pass
    return render(request, "transactions/bitcoin_details.html", {'details':details})