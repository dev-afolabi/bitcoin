from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):        
    return render(request, 'bitcoin_pages/index.html')

def about(request):        
    return render(request, 'bitcoin_pages/about-us.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = "message from: "+fullname+"\nSender email: "+from_email+"\n\n"+message

            try:
                send_mail(subject,full_message,'support@fonixcoin.com',['support@fonixcoin.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')       
    return render(request, 'bitcoin_pages/contact-us.html',{'form':form})

def faq(request):        
    return render(request, 'bitcoin_pages/faq.html')

def services(request):        
    return render(request, 'bitcoin_pages/services.html')

def bitcoin_ethereum(request):        
    return render(request, 'bitcoin_pages/bitcoin_and_ethereum.html')

def bitcoin_legality(request):        
    return render(request, 'bitcoin_pages/bitcoin_legality.html')

def coin_buy(request):        
    return render(request, 'bitcoin_pages/coin_buy_and_sell.html')

def crypto_trading(request):        
    return render(request, 'bitcoin_pages/crypto_trading.html')

def bitcoin_trading(request):        
    return render(request, 'bitcoin_pages/bitcoin_trading.html')

def security_ensure(request):        
    return render(request, 'bitcoin_pages/security_ensure.html')

def profile(request):        
    return render(request, 'bitcoin_pages/profile.html')

def refund_policy(request):        
    return render(request, 'bitcoin_pages/refund_policy.html')

def terms_and_condition(request):        
    return render(request, 'bitcoin_pages/terms_and_condition.html')

def fly(request):        
    return render(request, 'bitcoin_pages/fly.html')
