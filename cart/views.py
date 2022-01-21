from typing import NoReturn
from django.db.models.fields import DateField
from django.shortcuts import render, redirect
from .models import Cart, OrderPlaced, Orders, Payment
from json import dumps
import requests
import json
import time
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse


def index(request, str, name):
    url = 'https://firestore.googleapis.com/v1/projects/droppers-v1/databases/(default)/documents/items/' + \
        str + '/Products/'
    msg = requests.get(url)
    msg = msg.json()
    rawdata = json.dumps(msg)
    data = json.loads(rawdata)
    cats = []
    for i in data['documents']:
        cats.append(i['fields']['Product_Category']['stringValue'])
    uniCats = list(set(cats))
    uniCats.sort()

    product = Cart.objects.all()
    productId = []
    for i in product:
        productId.append(i.Product_Id)
    productId.sort()

    tc = product.count()
    # print(len(data['documents']))
    # venName = data['documents'][0]['fields']['Vendor_Name']['stringValue']+"";
    # venName = venName.replace(" ","")
    # if venName != name:
    #     return render(request,'cart/error.html',{})
    # else:
    #     return render(request,'cart/index.html',{"data": data['documents']})

    url1 = 'https://firestore.googleapis.com/v1/projects/droppers-v1/databases/(default)/documents/users/' + \
        str + '/'
    msg1 = requests.get(url1)
    msg1 = msg1.json()
    rawdata1 = json.dumps(msg1)
    data1 = json.loads(rawdata1)

    return render(request, 'cart/index.html', {"data": data['documents'], 'data1': data1['fields'], 'cats': uniCats, 'tc': tc, 'cart': productId, 'str': str, 'name': name})


def about(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/about.html', {'tc': tc})


def contact(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/contact.html', {'tc': tc})


def prodView(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/productview.html', {'tc': tc})


def myOrders(request):
    product = Cart.objects.all()
    tc = product.count()
    productPlaced = OrderPlaced.objects.all()
    prodPlace = Orders.objects.filter(confirm=True).order_by('-order_id')
    noOrder = prodPlace.count()
    orderIds = list(prodPlace)
    orderIds = json.dumps(orderIds, default=str)
    return render(request, 'cart/myorders.html', {"data": productPlaced, 'tc': tc, "prodPlace": prodPlace, 'noOrder': noOrder, 'Oid': orderIds})


def cart(request):

    milliseconds = round(time.time() * 1000)
    str = request.POST['str']
    name = request.POST['name']
    productId = request.POST['productId']
    productName = request.POST['productName']
    productCat = request.POST['productCat']
    productPrice = request.POST['productPrice']
    productDiscount = request.POST['productDiscount']
    productSellingPrice = request.POST['productSellingPrice']
    productImgUri = request.POST['productImgUri']
    productStatus = request.POST['productStatus']
    productQty = request.POST['productQty']
    productDesc = request.POST['productDesc']
    vendorId = request.POST['vendorId']

    # payload = {
    #     "fields": {
    #         "Customer_Name": {
    #             "stringValue": "CustomerName"
    #         },
    #         "Customer_Mob": {
    #             "stringValue": "9993733042"
    #         },
    #         "Customer_Address": {
    #             "stringValue": "Address"
    #         },
    #         "Vendor_Id": {
    #             "stringValue": vendorId
    #         },
    #         "Product_Id": {
    #             "stringValue": productId
    #         },
    #         "Product_Name": {
    #             "stringValue": productName
    #         },
    #         "Product_ImgUri": {
    #             "stringValue": productImgUri
    #         },
    #         "Product_Price": {
    #             "stringValue": productSellingPrice
    #         }
    #     }
    # }
    # payload = json.dumps(payload)
    # urlPost = 'https://firestore.googleapis.com/v1/projects/droppers-v1/databases/(default)/documents/Eorders/?documentId='+ str(milliseconds)
    # response = requests.post(urlPost, data=payload).json()

    product = Cart(
        Product_Id=productId,
        Product_Name=productName,
        Product_Category=productCat,
        Product_Price=productPrice,
        Product_Discount=productDiscount,
        Product_SellingPrice=productSellingPrice,
        Product_ImgUrl=productImgUri,
        Product_Status=productStatus,
        Product_Quantity=productQty,
        Product_Description=productDesc,
        VendorID=vendorId,
    )
    product.save()

    prod = Cart.objects.all()
    tc = prod.count()
    return redirect('Home', str=str, name=name)


def showCart(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/showcart.html', {"data": product, 'tc': tc})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        items_total = request.POST.get('itemsTotal', '')
        name = request.POST.get('fname', '') + request.POST.get('lname', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('mobile', '')
        order = Orders(items_json=items_json, items_total=items_total, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, mobile=phone)
        order.save()
        thank = "Order_Placed"
        id = order.order_id
        return render(request, 'cart/checkout.html', {'op': thank, 'id': id})
    return render(request, 'cart/checkout.html')


def checkoutDirect(request):
    productId = request.POST['productId']
    productName = request.POST['productName']
    productCat = request.POST['productCat']
    productPrice = request.POST['productPrice']
    productDiscount = request.POST['productDiscount']
    productSellingPrice = request.POST['productSellingPrice']
    productImgUri = request.POST['productImgUri']
    productStatus = request.POST['productStatus']
    productQty = request.POST['productQty']
    productDesc = request.POST['productDesc']
    vendorId = request.POST['vendorId']
    order = OrderPlaced(
        Product_Id=productId,
        Product_Name=productName,
        Product_Category=productCat,
        Product_Price=productPrice,
        Product_Discount=productDiscount,
        Product_SellingPrice=productSellingPrice,
        Product_ImgUrl=productImgUri,
        Product_Status=productStatus,
        Product_Quantity=productQty,
        Product_Description=productDesc,
    )
    order.save()
    return redirect('Myorders')


def search(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/search.html', {'tc': tc})


def account(request):
    product = Cart.objects.all()
    tc = product.count()
    # return render(request,'cart/account.html',{'tc':tc})
    return redirect('Register')


def errorpage(request):
    return render(request, 'cart/error.html', {})


def pay(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        items_total = request.POST.get('itemsTotal', '')
        name = request.POST.get('fname', '') + request.POST.get('lname', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('mobile', '')
        notes = {'Shipping address': address}
        client = razorpay.Client(
            auth=('rzp_test_PlEYg3Ud7QmRGo', 'xELzeSakL6gWRrNM2Of1wTBl'))
        payment = client.order.create(
            {'amount': float(items_total) * 100, 'currency': 'INR', 'payment_capture': 1, 'notes': notes})
        order = Orders(items_json=items_json, items_total=items_total, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, mobile=phone, payment_id=payment['id'])
        pay_id = Payment(name=name, amount=items_total,
                         payment_id=payment['id'])
        order.save()
        pay_id.save()
        return render(request, 'cart/pay.html', {'order': payment, 'email': email, 'phone': phone, 'custid': email+name})


@csrf_exempt
def pay_success(request):
    if request.method == "POST":
        a = request.POST
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        # print(order_id)
        payment = Payment.objects.filter(payment_id=order_id).first()
        order = Orders.objects.filter(payment_id=order_id).first()
        order.confirm = True
        payment.paid = True
        order.save()
        payment.save()
        prodPlace = Orders.objects.filter(confirm=True)
        noOrder = prodPlace.count()
        orderIds = list(prodPlace)
        orderIds = json.dumps(orderIds, default=str)
        thank = "Order_Placed"
        id = order.order_id
    return render(request, 'cart/myorders.html', {"prodPlace": prodPlace, 'noOrder': noOrder, 'Oid': orderIds, 'op': thank, 'id': id})


def register(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/register.html', {'tc': tc})


def login(request):
    product = Cart.objects.all()
    tc = product.count()
    return render(request, 'cart/login.html', {'tc': tc})
