from django.db import models

class Product(models.Model):
    gtin = models.CharField(max_length=14, unique=True)  # məhsulun unikal kodu
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True, null=True)
    product_type = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    producer = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.gtin})"
