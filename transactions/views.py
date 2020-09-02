from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import DepositForm, WithdrawalForm
from .models import Withdrawal,User,Deposit
from payment_details.models import BTCTransfer, BankTransfer, Notification, Message


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

            subject = "Deposit Request"
            message = render_to_string('transactions/deposit_message.html',{
                'user':request.user,
                'amount':deposit.amount
            })
            to_email = 'jmlindhagen@gmail.com'
            email = EmailMessage(subject,message, to=[to_email])
            email.send()

            if deposit.payment_option == "Bank Transfer":
                return redirect("bank-details")
            else:
                return redirect("bitcoin-details")

        context = {
                    "title": title,
                    "form": form,
                    "notifications":notifications,
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
                if withdrawal.user.bonus >= withdrawal.amount:
                    withdrawal.user.bonus -= withdrawal.amount
                    withdrawal.user.save()
                    withdrawal.save()
                    Notification.objects.create(user=request.user, message=withdrawal_message)
                else:
                    withdrawal.user.balance -= withdrawal.amount
                    withdrawal.user.save()
                    withdrawal.save()
                    Notification.objects.create(user=request.user, message=withdrawal_message)

                subject = "Withdrawal Request"
                message = render_to_string('transactions/withdrawal_message.html',{
                    'user':request.user,
                    'amount':withdrawal.amount
                })
                to_email = 'jmlindhagen@gmail.com'
                email = EmailMessage(subject,message, to=[to_email])
                email.send()

                client_subject = "Withdrawal Request"
                client_message = render_to_string('transactions/client_withdrawal_message.html',{
                    'user':request.user,
                    'amount':withdrawal.amount
                })
                client_to_email = request.user.email
                client_email = EmailMessage(client_subject,client_message, to=[client_to_email])
                client_email.send()

        
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