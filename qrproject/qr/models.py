from django.db import models
from django.core.validators import RegexValidator

class Product(models.Model):
    gtin = models.CharField(
    max_length=14,
    unique=True,
    validators=[
        RegexValidator(r'^\d{8,14}$', 'GTIN yalnız 14 rəqəm  ola biler.')
    ]
    )
    
    name = models.CharField(max_length=255)
    year = models.IntegerField(max_length=10, blank=True, null=True)
    product_type = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    producer = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.gtin})"
