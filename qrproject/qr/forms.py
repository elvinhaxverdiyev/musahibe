from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['gtin', 'name', 'year', 'product_type', 'volume', 'producer', 'description', 'ingredients', 'image']
