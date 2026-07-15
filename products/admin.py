from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = (
        'id',
        'name',
        'description',
        'price',
        'stock',
        'category',
        'status',
    )