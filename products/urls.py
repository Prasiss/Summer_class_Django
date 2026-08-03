from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),        
    path('<int:id>/',views.product_details, name='product_detail'),
    path('addtocart/',views.add_to_cart, name='add_to_cart'),
    path('checkout/',views.checkout, name='checkout'),
]   