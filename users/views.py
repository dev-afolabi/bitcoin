from django.shortcuts import render,redirect
from django.contrib.auth import (get_user, get_user_model, logout, login, authenticate)
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.contrib.messages import error, success
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import UserLoginForm
from payment_details.models import Notification

# Create your views here.
user_creation_message = "Welcome to Bitfonix!!! we're happy to have you here"

User = get_user_model()

@sensitive_post_parameters('password1','password2')
def signup(request):
    if request.method == 'POST':
        bound_form = UserCreationForm(request.POST or None,
                                    request.FILES or None)
        if bound_form.is_valid():
            user = bound_form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your Bitfonix Account"
            if request.is_secure():
                protocol = 'https'
            else:
                protocol = 'http'
            message = render_to_string('registration/email_create.html',{
                'user':user,
                'site_name':current_site,
                'protocol':protocol,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = bound_form.cleaned_data.get('email')
            email = EmailMessage(subject,message, to=[to_email])
            email.send()
            return redirect('my-auth:create_done')
    else:
        bound_form = UserCreationForm()
    return render(request, 'registration/user_create.html', {'form':bound_form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.email_confirmed = True
        user.Save()
        Notification.objects.create(user=user, message=user_creation_message)
        messages.success(request, 'You Account has been successfully activated, please login')
        return redirect('my-auth:activated')
    else:
        user.delete()
        return render(request, 'registration/user_activate_failed.html')

def account_activation_sent(request):
    return render(request, 'registration/user_create_done.html')

def account_activated(request):
    return render(request, 'registration/user_activated.html')

def login_view(request):  # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        title = "Load Account Details"
        form = UserLoginForm(
            request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            user_obj = User.objects.filter(email=email).first()
            password = form.cleaned_data.get("password")
            # authenticates Email & Password
            user = authenticate(email=user_obj.email, password=password)
            login(request, user)
            return redirect("dashboard")

        context = {"form": form,
                   "title": title
                   }

        return render(request, "registration/login.html", context)
