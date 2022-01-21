from django.urls import path
from . import views

urlpatterns = [
    path('<slug:name>/<slug:str>/home/', views.index, name='Home'),
    path('', views.about, name='About'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('productView/', views.prodView, name='ProductView'),
    path('cart/', views.cart, name='Cart'),
    path('showCart/', views.showCart, name='ShowCart'),
    path('checkout/', views.checkout, name='Checkout'),
    path('checkoutDirect/', views.checkoutDirect, name='CheckoutDirect'),
    path('myOrders/', views.myOrders, name='Myorders'),
    path('search/', views.search, name='Search'),
    path('account/', views.account, name='Account'),
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='Register'),
    path('error/', views.errorpage, name='error'),

   #  path('paymentdone/', views.payment_done, name='paymentdone'),
    path('pay/', views.pay, name='Pay'),
    path('pay-success/', views.pay_success, name='Pay-Success'),
]
