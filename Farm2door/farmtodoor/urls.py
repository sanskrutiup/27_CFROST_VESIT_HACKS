from django.contrib import admin
from django.urls import path
from farmtodoor import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop_details', views.details, name='shop_details'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('paytm_payment', views.paytm_payment, name='paytm_payment'),
]