from django.contrib.auth import get_user_model 
import datetime
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth import authenticate
from django.forms.widgets import Select
from django.forms import ModelForm

from .models import User


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
            super(BaseUserCreationForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.pop("autofocus",None)

    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-input','align':'center', 'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class': 'form-input','align':'center', 'placeholder':'Comfirm Password'}))
    
    class Meta:
        model = get_user_model()
        fields = ["first_name",
                  "last_name",
                  "gender",
                  "email",
                  "password1",
                  "password2",
                  "picture"
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-input', 'placeholder':'first name'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-input', 'placeholder':'last name'}),
            'email' : forms.EmailInput(attrs={'class': 'form-input', 'placeholder':'your email'}),
            'gender' : Select(attrs={'class': 'form-input'}),
        }
        

        def save(self, commit=True):
            user = super(BaseUserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user

class UserLoginForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-input form-group','align':'center', 'placeholder':'Email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-input form-group','align':'center', 'placeholder':'Password'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user_obj = User.objects.filter(email=email).first()
            if user_obj:
                user = authenticate(email=user_obj.email, password=password)
                if not user:
                    raise forms.ValidationError("Password Does not Match")
                if not user.is_active:
                    raise forms.ValidationError("Account is not Active.")
            else:
                raise forms.ValidationError("Account Does Not Exist.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class EditUserForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ["first_name",
                  "last_name",
                  "gender",
                  "email",
                  "picture"
                  ]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : Select(attrs={'class': 'form-control'}),
        }


    
