from django.shortcuts import render, HttpResponse
import json
import uuid
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

def paytm_payment(request):
    # Your Paytm merchant key and ID
    MERCHANT_KEY = 'LeXyP7zzLpszQD%%'
    MERCHANT_ID = 'lKESvj23798844173102'
    unique_number = str(uuid.uuid4().int)

    # Get payment data from POST request
    amount = 200
    email = 'shree.samal1502@gmail.com'
    phone = '1234567890'

    # Generate Paytm checksum
    data_dict = {
        'MID': MERCHANT_ID,
        'ORDER_ID': unique_number,
        'TXN_AMOUNT': str(amount),
        'CUST_ID': email,
        'MOBILE_NO': phone,
    }
    checksum = paytmchecksum.generate_checksum(data_dict, MERCHANT_KEY)

    # Return JSON response with checksum and other data
    response_data = {
        'checksum': checksum,
        'MID': MERCHANT_ID,
        'ORDER_ID': unique_number,
        'TXN_AMOUNT': str(amount),
        'CUST_ID': email,
        'MOBILE_NO': phone,
    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def paytm_response(request):
    # Your Paytm merchant key and ID
    MERCHANT_KEY = 'LeXyP7zzLpszQD%%'
    MERCHANT_ID = 'lKESvj23798844173102'

    # Get response data from POST request
    data_dict = {}
    for key in request.POST:
        data_dict[key] = request.POST[key]

    # Verify Paytm checksum
    if paytmchecksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH']):
        # Payment was successful
        # Update payment status in your database
        return HttpResponse('Payment Successful')
    else:
        # Payment failed
        # Handle payment failure
        return HttpResponse('Payment Failed')