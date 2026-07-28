from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

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
    readonly_fields = ('image_preview',)
    
    def image_preview(elf,obj):
        if obj.product_image:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px style="object-fit:cover";" />', obj.product_image.url)
        return "No Image"
    image_preview.short_description = 'Product Image Preview'
    
    