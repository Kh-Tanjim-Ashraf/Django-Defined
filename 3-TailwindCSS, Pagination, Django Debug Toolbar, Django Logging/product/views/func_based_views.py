from django.shortcuts import render
from product.models import Product

def productList(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(
        request=request,
        template_name='./product/fbv/product-list.html',
        context=context
    )
