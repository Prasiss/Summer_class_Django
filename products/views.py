from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Product,Category
from django.core.paginator import Paginator
from carts.models import CartItem
from carts.views import _cart_id
from django.db.models import Q
# Create your views here.

def products(request,category_slug=None):
    cateogories =None
    products=None
    if category_slug != None:
        cateogories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=cateogories,available=True)
        paginator = Paginator(products, 3)
        page= request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = len(paged_products)
        
    else:
        products = Product.objects.all().filter(status=True)
        paginator = Paginator(products, 3)
        page= request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = len(paged_products)
        
    context={
        'products':paged_products,
        'product_count':product_count,
    }
    return render(request, 'main/products.html', context)
    
def product_details(request,category_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=product).exists()
        
    except Product.DoesNotExist:
        raise Http404 ('Product not found')
    context={
        'product':product,
        'in_cart':in_cart
    }
    
    return render(request, 'main/product_details.html',context)

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

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def search(request):
    if 'keyword' in request.GET:
        keyword= request.GET.get('keyword','').strip()
        products=Product.objec.none()
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q (description_iconatins=keyword) | Q (product_name__icontains=keyword)
                 
            )
        context={
            'products':products,
            'products_count':products.count()
        }
        return render(request,'main/products.html')
        