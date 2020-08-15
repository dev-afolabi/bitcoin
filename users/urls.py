from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (RedirectView, TemplateView)
from .forms import UserLoginForm

from .views import *

app_name = "my-auth"

password_urls = [
    url(r'^change/$', auth_views.PasswordChangeView.as_view(), 
    name="password_change"),

    url(r'^change/done/$', auth_views.PasswordChangeDoneView.as_view(), 
    name="password_change_done"),

    url(r'^reset/$', auth_views.PasswordResetView.as_view(), 
    name="password_reset"),

    url(r'^reset/sent/$', auth_views.PasswordResetDoneView.as_view(), 
    name="password_reset_done"),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', auth_views.PasswordResetConfirmView.as_view(), 
    name="password_reset_confirm"),

    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(), 
    name="password_change_complete"),
]

urlpatterns = [
    url(r'^login/$', login_view, name='login'),

    path('logout/', 
    auth_views.LogoutView.as_view(),
    {
        'extra_context': {'form': AuthenticationForm}
    },
    name="logout"),

    url(r'^password/', include(password_urls)), 
    url(r'create/$', signup, name='create'),
    url(r'^create/done/$', account_activation_sent, name='create_done'),
    url(r'^activation/successfull/$', account_activated, name='activated'),

    path('activate/<uidb64>/<token>/', activate, 
    name='activate'),
    
]

