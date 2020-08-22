from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^inbox$', inbox, name='inbox'),
    url(r'^message/(?P<pk>[-a-zA-Z0-9]+)/$', read_mail, name='read_mail'),
    url(r'^compose$', compose, name='compose'),
]