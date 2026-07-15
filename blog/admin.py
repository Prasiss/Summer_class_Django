from django.contrib import admin
from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at',)
    list_display = (
        'title',
        'content',
    )