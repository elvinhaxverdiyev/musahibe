from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
import os

# Məhsul əlavə etmək və QR yaratmaq
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()

            # Dinamik URL: HTML səhifəyə yönləndirir
            host = request.get_host()
            url = f"http://{host}/product/{product.gtin}/"

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
    host = request.get_host()
    url = f"http://{host}/product/{gtin}/"

    img = qrcode.make(url)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")
