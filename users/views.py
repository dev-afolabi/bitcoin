from django.shortcuts import render,redirect
from django.contrib.auth import (get_user, get_user_model, logout)
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.contrib.messages import error, success
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

# Create your views here.

User = get_user_model()

# class ActivateAccount(View):
#     @method_decorator(never_cache)
#     def get(self, request, uidb64, token):
#         User = get_user_model()
#         try:
#             uid = force_text(
#                 urlsafe_base64_encode(uidb64)
#             )
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         if (user is not None and token_generator.check_token(user, token)):
#             user.is_active = True
#             user.save()
#             success(
#                 request,
#                 'Account Activted Succesfully! '
#                 'You may now login.'
#             )
#             return redirect(self.success_url)
#         else:
#             return TemplateResponse(
#                 request,
#                 self.template_name
#             )

# class CreateAccount(View):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('create_done')
#     template_name = 'registration/user_create.html'

#     def get(self, request):
#         return TemplateResponse(
#             request,
#             self.template_name,
#             {'form':self.form_class()}
#         )

#     @method_decorator(sensitive_post_parameters('password1','password2'))
#     def post(self, request):
#         bound_form = self.form_class(request.POST)
#         if bound_form.is_valid():
#             user = bound_form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = "Activate your Bitfonix Account"
#             message = render_to_string('email_create.html',{
#                 'user':user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_decode(force_bytes(user.pk)),
#                 'token':account_activate_token.make_token(user)
#             })
#             user.email_user(subject, message)
#             return redirect(success_url)
#         return TemplateResponse(
#             request,
#             self.template_name,
#             {'form':bound_form}
#         )


@sensitive_post_parameters('password1','password2')
def signup(request):
    if request.method == 'POST':
        bound_form = UserCreationForm(request.POST)
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
            return redirect('create_done')
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
        return redirect('login')
    else:
        return render(request, 'registration/user_activate_failed.html')

def account_activation_sent(request):
    return render(request, 'registration/user_create_done.html')
