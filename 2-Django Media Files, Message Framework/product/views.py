from django.shortcuts import render, redirect
from product.forms.product_model_form import ProductForm
from .models import Product


def productList(request):
    products = Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/index.html',
        context=context
    )


def productCreate(request):
    if request.method == 'POST':
        # Bind the data to the form
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list-FBV')
    else:
        form = ProductForm()
    context={'form':form}
    return render(
        request=request,
        template_name='product/create-product.html',
        context=context
    )