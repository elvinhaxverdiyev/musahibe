from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'gtin': 'GTIN',
            'name': 'Ad',
            'year': 'İl',
            'product_type': 'Növ',
            'volume': 'Həcm',
            'producer': 'İstehsalçı',
            'description': 'Təsvir',
            'ingredients': 'Tərkibi',
            'image': 'Şəkil',  
        }