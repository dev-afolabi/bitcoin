from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(label="Fullname",widget=forms.TextInput(attrs={'placeholder':'Your Fullname'}),max_length=100)
    from_email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'placeholder':'Your Email'}))
    subject = forms.CharField(label="Subject",widget=forms.TextInput(attrs={'placeholder':'Subject'}),max_length=300)
    message = forms.CharField(label="message",widget=forms.Textarea(attrs={'placeholder':'Your Message'}))