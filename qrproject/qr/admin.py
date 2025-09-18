from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'gtin', 'year', 'product_type', 'volume', 'producer')
    search_fields = ('name', 'gtin', 'producer')
    list_filter = ('year', 'product_type', 'producer')
    readonly_fields = ('gtin',) 
