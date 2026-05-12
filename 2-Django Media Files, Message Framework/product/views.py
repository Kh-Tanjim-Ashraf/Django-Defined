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
        form = ProductForm(data=request.POST, files=request.FILES)
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


def productUpdate(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        # Bind the data to form
        form=ProductForm(data=request.POST)
        # Update the record if the form validates without error
        if form.is_valid():
            data=ProductForm(data=request.POST, instance=product)
            data.save()
            return redirect('product-list-FBV')
    else:
        form=ProductForm(instance=product)

    context={
        'form':form,
        'product':product
    }

    return render(
        request=request,
        template_name='product/update-product.html',
        context=context
    )


def productDelete(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list-FBV')
    context={'product':product}
    return render(
        request=request,
        template_name='product/delete-product.html',
        context=context
    )