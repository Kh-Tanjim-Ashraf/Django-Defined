from django.shortcuts import render, redirect
from product.forms.product_model_form import ProductForm
from product.models import Product
from django.contrib import messages


def productList(request):
    products = Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/fbv_templates/list-product.html',
        context=context
    )


def productCreate(request):
    if request.method == 'POST':
        # Bind the data to the form
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request=request, message=f"{form.cleaned_data.get('name')}: Product created successfully!")
            return redirect('FBV_PRODUCT:product-list-FBV')
    else:
        form = ProductForm()
    context={'form':form}
    return render(
        request=request,
        template_name='product/fbv_templates/create-product.html',
        context=context
    )


def productUpdate(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        # Bind the data to form
        # IMPORTANT: Files are required to send along w/ the request.POST data, in order to validate the media files. Otherwise, instead of displaying message regarding media-file errors, Django will encounter program crash displaying the data could not be updated since it could not be validated (because of the files are yet to validate)
        form=ProductForm(data=request.POST, files=request.FILES)
        # Update the record if the form validates without error
        if form.is_valid():
            data=ProductForm(data=request.POST, files=request.FILES, instance=product)
            data.save()
            messages.success(request=request, message=f"{form.cleaned_data.get('name')}: Product updated successfully!")
            return redirect('FBV_PRODUCT:product-list-FBV')
    else:
        form=ProductForm(instance=product)

    context={
        'form':form,
        'product':product
    }

    return render(
        request=request,
        template_name='product/fbv_templates/update-product.html',
        context=context
    )


def productDelete(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request=request, message=f"{product.name}: Product deleted successfully!")
        return redirect('FBV_PRODUCT:product-list-FBV')
    context={'product':product}
    return render(
        request=request,
        template_name='product/fbv_templates/delete-product.html',
        context=context
    )