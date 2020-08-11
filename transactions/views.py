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
from payment_details.models import BTCTransfer, BankTransfer


@login_required()
def deposit_view(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Deposit"
        form = DepositForm(request.POST or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user

            # adds users deposit to balance.
            # deposit.user.balance += deposit.amount
            # deposit.user.save()
            deposit.save()
            messages.success(request, 'Your deposit will be proccesed when funds have been posted'
                             .format(deposit.amount))
            if deposit.payment_option == "Bank Transfer":
                return redirect("bank-details")
            else:
                return redirect("bitcoin-details")

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "transactions/form.html", context)


@login_required()
def withdrawal_view(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
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
                messages.error(request, 'You Have Transfered {} €.'
                               .format(withdrawal.amount))
                return redirect("dashboard")

            else:
                messages.error(
                    request,
                    'You Can Not Transfer More Than Your Balance.'
                    )

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "transactions/form.html", context)
@login_required
def bank_payment_details(request):
    try:
        details = BankTransfer.objects.get(name='account')
    except ObjectDoesNotExist:
        pass
    return render(request, "transactions/bank_details.html", {'details':details})

@login_required
def bitcoin_payment_details(request):
    try:
        details = BTCTransfer.objects.get(name='my wallet')
    except ObjectDoesNotExist:
        pass
    return render(request, "transactions/bitcoin_details.html", {'details':details})