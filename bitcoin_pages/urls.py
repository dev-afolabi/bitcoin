from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about-us$', about, name='about-us'),
    url(r'^contact-us$', contact, name='contact'),
    url(r'^frequently-asked-question$', faq, name='faq'),
    url(r'^services$', services, name='services'),
    url(r'^bitcoin-and-ethereum$', bitcoin_ethereum, name='bitcoin_ethereum'),
    url(r'^bitcoin-legality$', bitcoin_legality, name='bitcoin_legality'),
    url(r'^bitcoin-trading$', bitcoin_trading, name='bitcoin_trading'),
    url(r'^coin-buy-and-sell$', coin_buy, name='coin_buy'),
    url(r'^crypto-trading$', crypto_trading, name='crypto_trading'),
    url(r'^company-profile$', profile, name='profile'),
    url(r'^security-ensure$', security_ensure, name='security_ensure'),
    url(r'^refund-policy$', refund_policy, name='refund_policy'),
    url(r'^terms-and-condition$', terms_and_condition, name='terms_and_condition'),
]