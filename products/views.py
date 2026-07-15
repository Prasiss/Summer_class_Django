from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product,Category

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html',{'products':products})
    
def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/detail.html',{'product': product})

