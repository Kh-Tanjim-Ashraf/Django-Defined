from django.shortcuts import render
from product.models import Product


def productList(request):
    products = Product.objects.all()
    return render(
        request=request,
        template_name='list.html',
        context={'products': products}
    )
