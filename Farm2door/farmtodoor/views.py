from django.shortcuts import render, HttpResponse

# Create your views here.
def  index(request):
    # context = {
    #     'variable' : "Hello"
    # }
    return render(request, 'index.html')

def  shop(request):
    return render(request, 'shop-grid.html')

def  details(request):
    return render(request, 'shop-details.html')

def  cart(request):
    return render(request, 'shoping-cart.html')

def  contact(request):
    return render(request, 'contact.html')

def  checkout(request):
    return render(request, 'checkout.html')
