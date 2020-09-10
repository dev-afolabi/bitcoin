from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    fullname = forms.CharField(label="Fullname",widget=forms.TextInput(attrs={'placeholder':_('Your Fullname')}),max_length=100)
    from_email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'placeholder':_('Your Email')}))
    subject = forms.CharField(label="Subject",widget=forms.TextInput(attrs={'placeholder':_('Subject')}),max_length=300)
    message = forms.CharField(label="message",widget=forms.Textarea(attrs={'placeholder':_('Your Message')}))