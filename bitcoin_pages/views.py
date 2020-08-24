from django.shortcuts import render

# Create your views here.
def index(request):        
    return render(request, 'bitcoin_pages/index.html')

def about(request):        
    return render(request, 'bitcoin_pages/about-us.html')

def contact(request):        
    return render(request, 'bitcoin_pages/contact-us.html')

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
