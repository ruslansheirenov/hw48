from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category']
    list_filter = ['product_name']
    search_field = ['category']
    fields = ['product_name', 'category', 'description', 'remainder', 'price']

admin.site.register(Product, ProductAdmin)