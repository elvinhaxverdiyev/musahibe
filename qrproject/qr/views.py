from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from barcode import Code128
from barcode.writer import ImageWriter
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
import os


# AWS public IP və ya domain
AWS_PUBLIC_HOST = "http://16.170.243.177:8000"

# Məhsul əlavə etmək və QR yaratmaq
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            # QR URL-i: sadəcə /01/<gtin>/ və AWS public IP ilə
            url = f"{AWS_PUBLIC_HOST}/01/{product.gtin}/"

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


def product_detail(request, gtin):
    product = get_object_or_404(Product, gtin=gtin)

    # Barkod mətni (GS1-də Application Identifier 01 + GTIN)
    barcode_text = f"01{product.gtin}"

    # Barkod fayl adı və yolu
    barcode_filename = f"barcode_{product.gtin}.png"
    barcode_path = os.path.join(settings.MEDIA_ROOT, barcode_filename)

    # Əgər barkod şəkli yoxdursa, yarat
    if not os.path.exists(barcode_path):
        Code128(barcode_text, writer=ImageWriter()).save(
            barcode_path.replace(".png", "")
        )

    # Template üçün URL
    barcode_url = f"{settings.MEDIA_URL}{barcode_filename}"

    return render(request, "product_detail.html", {
        "product": product,
        "barcode_url": barcode_url
    })

# QR kodu browserdə görmək üçün (optional)
def create_qr(request, gtin):
    url = f"{AWS_PUBLIC_HOST}/01/{gtin}/"
    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type="image/png")
