from django.shortcuts import render
from product.models import Product


def productIndex(request):
    products = Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/index.html',
        context=context
    )

