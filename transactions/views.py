from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import DepositForm, WithdrawalForm
# from formtools.wizard.views import SessionWizardView
from .models import Withdrawal,User,Deposit


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
            deposit.user.save()
            deposit.save()
            messages.success(request, 'Your deposit will be proccesed when funds have been posted'
                             .format(deposit.amount))
            return redirect("dashboard")

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


# class FormWizard(SessionWizardView):
#     template_name = "transactions/form.html"
#     # def dispatch(self, request, *args, **kwargs):
#     #     return super(FormWizard,self).dispatch(request, *args, **kwargs)
    

#     def get_form_instance(self,step):
#         return self.instance_dict.get(step,None)

#     def done(self, form_list, **kwargs):
#         withdrawal = Withdrawal()
#         otp = Otp()
#         withdrawal.user = self.request.user
#         otp.user = self.request.user
#         for form in form_list:
#             for k,v in form.cleaned_data.items():
#                 setattr(withdrawal,k,v)
        
#         for form in form_list:
#             for k,v in form.cleaned_data.items():
#                 setattr(otp,k,v)

#         otp.save()

#         allowed = True
#         while allowed:

#             #otp for 3 day transaction
#             if otp.one_time_password in withdrawal.user.otp_value1:

#                 if withdrawal.user.balance >= withdrawal.amount:


#                     withdrawal.user.balance -= withdrawal.amount
#                     withdrawal.user.save()
#                     withdrawal.save()
#                     messages.error(self.request, 'You have Transfered {} €.'
#                                     .format(withdrawal.amount))
#                     allowed = False
#                     return redirect("dashboard")

#                 else:
#                     messages.error(self.request,
#                     'You Can Not Transfer More Than Your Balance.')
#                     allowed = False
#                     return super(FormWizard, self).render(form, **kwargs)

#             #otp for 7 days transactions
#             elif otp.one_time_password in withdrawal.user.otp_value2:

#                 if withdrawal.user.balance >= withdrawal.amount:


#                     withdrawal.user.balance -= withdrawal.amount
#                     withdrawal.user.save()
#                     withdrawal.save()
#                     messages.error(self.request, 'You Have Transfered {} €.'
#                                     .format(withdrawal.amount))
#                     allowed = False
#                     return redirect("dashboard")

#                 else:
#                     messages.error(self.request,
#                     'You Can Not Transfer More Than Your Balance.')
#                     allowed = False
#                     return super(FormWizard, self).render(form, **kwargs)

#             #otp for 14 days transaction
#             elif otp.one_time_password in withdrawal.user.otp_value3:

#                 if withdrawal.user.balance >= withdrawal.amount:

#                     withdrawal.user.balance -= withdrawal.amount
#                     withdrawal.user.save()
#                     withdrawal.save()
#                     messages.error(self.request, 'You Have Transfered {} €.'
#                                     .format(withdrawal.amount))
#                     allowed = False
#                     return redirect("dashboard")

#                 else:
#                     messages.error(self.request,
#                     'You Can Not Transfer More Than Your Balance.')
#                     allowed = False
#                     return super(FormWizard, self).render(form, **kwargs)
                    
                    

#             else:
#                 messages.error(self.request, 'You have entered a wrong otp'
#                                 .format(withdrawal.amount))
#                 return super(FormWizard, self).render(form, **kwargs)
