from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),

    path('my-orders/', views.my_orders, name='my_orders'),
    path('inbox/', views.inbox, name='inbox'),
    path('my-sales/', views.my_sales, name='my_sales'),

    path('change-password/', views.change_password, name='change_password'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('my-request/', views.sent_messages, name='sent_messages'),
    path('my-request-received/', views.message_details, name='message_details'),
    
    path('login/', views.login, name='Login'),
    path('register/', views.register, name='register'),

    path('sent/', views.sent, name='sent'),
    path('cateogory/<slug:category_slug>/', views.products, name='category_products'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
]