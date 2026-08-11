from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'main/products.html',{'products':products})
    
def product_details(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'main/product_details.html',{'product':product})

def add_to_cart(request):
    return render(request, 'main/addtocart.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def dashboard(request):
    return render(request, 'main/accounts/dashboard.html')


def add_product(request):
    return render(request, 'main/accounts/add-product.html')


def edit_product(request):
    return render(request, 'main/accounts/edit-product.html')


def my_orders(request):
    return render(request, 'main/accounts/my-orders.html')


def inbox(request):
    return render(request, 'main/accounts/inbox.html')


def my_sales(request):
    return render(request, 'main/accounts/my-sales.html')


def change_password(request):
    return render(request, 'main/accounts/change-password.html')


def my_profile(request):
    return render(request, 'main/accounts/edit-profile.html')


def sent_messages(request):
    return render(request, 'main/accounts/my-request.html')


def message_details(request):
    return render(request, 'main/accounts/my-request-received.html')


def edit_profile(request):
    return render(request, 'main/accounts/edit_profile.html')


def sent(request):
    return render(request, 'main/accounts/sent.html')