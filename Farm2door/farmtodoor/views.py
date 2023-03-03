from django.shortcuts import render, HttpResponse
from datetime import datetime
from farmtodoor.models import Reg
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def  register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = fname + ' ' + lname
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        userType = request.POST.get('userType')
        birth_date = request.POST.get('birth_date')
        password = request.POST.get('password')
        
        reg = Reg(name=name, email=email, contact=contact, gender=gender, address=address, city=city, state=state, pincode=pincode, birth_date=birth_date, userType=userType, password=password)
        reg.save()
        
    return render(request, 'reg.html')

@csrf_exempt
def  login(request):
    return render(request, 'login.html')