from django.contrib import admin
from django.urls import path
from farmtodoor import views

urlpatterns = [
    # Customers
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop_details', views.details, name='shop_details'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('register', views.register, name='register'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('razorpay_pay', views.razorpay_pay, name='razorpay_pay'),
    
    
    # Farmers
    path('farmer/home', views.farmer_home, name='farmer_home'),
    path('farmer/add/product', views.farmer_addprod, name='farmer_addprod'),
]