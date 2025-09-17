from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
import os
from django.urls import reverse

# Məhsul əlavə etmək və QR yaratmaq
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()

            # Dinamik URL: HTML səhifəyə yönləndirir
            # Burada QR scan ediləndə /01/<gtin>/ açılacaq
            url = request.build_absolute_uri(reverse("product-detail", args=[product.gtin]))

            # QR kod şəkli yarat
            qr = qrcode.make(url)
            qr_path = os.path.join(settings.MEDIA_ROOT, f"qr_{product.gtin}.png")
            qr.save(qr_path)

            return render(request, "product_success.html", {
                "product": product,
                "qr_url": f"{settings.MEDIA_URL}qr_{product.gtin}.png"
            })
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form})

# Telefon scan edəndə açılacaq HTML səhifə
def product_detail(request, gtin):
    product = get_object_or_404(Product, gtin=gtin)
    return render(request, "product_detail.html", {"product": product})

# QR kodu browserdə görmək üçün (optional)
def create_qr(request, gtin):
    # Burada da /01/<gtin>/ URL-i yaradılır
    url = request.build_absolute_uri(reverse("product-detail", args=[gtin]))

    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")
