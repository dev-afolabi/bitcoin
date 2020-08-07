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
