from django.shortcuts import render
from product.models import Product


def productList(request):
    context = {'products': Product.objects.all()}
    return render(
        request=request, 
        template_name='product/list.hmtl',
        context=context
    )