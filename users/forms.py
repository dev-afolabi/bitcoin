from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
import datetime
from django import forms
from django.contrib.auth import authenticate
from django.forms.widgets import Select

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name",
                  "last_name",
                  "gender",
                  "email",
                  "password1",
                  "password2",
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'gender' : Select(attrs={'class': 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user

class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user_obj = User.objects.filter(email=email).first()
            if user_obj:
                user = authenticate(email=user_obj.email, password=password)
                if not user:
                    raise forms.ValidationError("Account Does Not Exist.")
                if not user.check_password(password):
                    raise forms.ValidationError("Password Does not Match.")
                if not user.is_active:
                    raise forms.ValidationError("Account is not Active.")
            else:
                raise forms.ValidationError("Account Does Not Exist.")

        return super(UserLoginForm, self).clean(*args, **kwargs)