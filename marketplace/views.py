from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product,Category
from blog.models import Blog

def home(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()
    cateogories=Category.objects.all()
    banner=Product.objects.all().filter(status=True)
    return render (request, 'main/home.html', {'products':products, 'blogs':blogs, 'categories':cateogories, 'banner':banner})
