from django.shortcuts import render, redirect
from product.forms.model_forms import ProductForm
from product.models import Product

def productIndex(request):
    products=Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/django_form_based_crud/index.html',
        context=context
    )


def productCreate(request):
    if request.method == 'POST':
        data = ProductForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('product-list-dj-form')
    form=ProductForm()
    context={'form':form}
    return render(
        request=request,
        template_name='product/django_form_based_crud/create-product.html',
        context=context
    )
