from django.conf.urls import url
from .forms import WithdrawalForm
# from .views import FormWizard

from .views import deposit_view, withdrawal_view,bank_payment_details, bitcoin_payment_details

urlpatterns = [
    url(r'^deposit/$', deposit_view, name='deposit'),
    url(r'^withdrawal/$', withdrawal_view, name='withdraw'),
    url(r'^bank-details/$',bank_payment_details, name='bank-details'),
    url(r'^bitcoin-details/$',bitcoin_payment_details, name='bitcoin-details')
    # url(r'^Transactions/$' , FormWizard.as_view([ WithdrawalForm, OtpForm]), name='test'),
]