from django.conf.urls import url
from .forms import WithdrawalForm
# from .views import FormWizard

from .views import deposit_view, withdrawal_view

urlpatterns = [
    url(r'^deposit/$', deposit_view, name='deposit'),
    url(r'^withdrawal/$', withdrawal_view, name='withdrawal'),
    # url(r'^Transactions/$' , FormWizard.as_view([ WithdrawalForm, OtpForm]), name='test'),
]