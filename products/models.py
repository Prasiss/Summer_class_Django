from django.db import models

# Create your models here.
from django.urls import reverse
 
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='photos/products',blank=True)
    featured_product = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.name
    