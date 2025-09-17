from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_product, name="create-product"),
    path("1/product/<str:gtin>/", views.product_detail, name="product-detail"),

]
