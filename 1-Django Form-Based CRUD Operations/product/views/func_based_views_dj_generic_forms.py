from django.shortcuts import render, redirect
from product.models import Product
from product.forms.generic_forms import ProductFormGen


def productIndex(request):
    products = Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/index.html',
        context=context
    )


def productCreate(request):
    if request.method == 'POST':
        form = ProductFormGen(request.POST)
        if form.is_valid():
            # Execute some logic
            return redirect('product-list-dj-gen-form')
    else:
        form=ProductFormGen()        
        
    context={'form':form}
    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/create-product.html',
        context=context
    )