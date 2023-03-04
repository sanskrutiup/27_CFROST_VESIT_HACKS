from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from farmtodoor.models import Reg, AddProd
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
import razorpay

# Create your views here.
def  index(request):
    # if request.user.is_anonymous:
    #     return redirect("/loginUser")
    home_products = AddProd.objects.all()
    data = {
        "home_products" : home_products
    }
    
    return render(request, 'index.html', data)

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
def  loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(email=email, password=password)
        print(request.user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@csrf_exempt
def  logoutUser(request):
    return redirect("/loginUser")

@csrf_exempt
def  razorpay_pay(request):
    client = razorpay.Client(auth = ("rzp_test_HJEVdhoCF6dSvY", "xpocHyKYqLG8FJZrNRR6LOPe"))
    payment = client.order.create({'amount': 200 * 100, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, 'razorpay_pay.html', payment)



# Farmer
@csrf_exempt
def farmer_home(request):
    return render(request, 'farmer_home.html')

@csrf_exempt
def farmer_addprod(request):
    if request.method == "POST":
        prodType = request.POST.get('prodType')
        prodName = request.POST.get('prodName')
        total_weight = int(request.POST.get('total_weight'))
        price = int(request.POST.get('price'))
        quantity = total_weight/0.5
        email = "abc@gmail.com"
        proddesc = "Get Freshly farmed " + prodName + " at your home"
        
        addProd = AddProd(prodType=prodType, prodName=prodName, total_weight=total_weight, price=price, proddesc=proddesc, quantity=quantity, email=email)
        addProd.save()
    return render(request, 'farmer_addprod.html')


# python manage.py migrate --run-syncdb