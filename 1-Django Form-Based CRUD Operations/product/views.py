from django.shortcuts import render, redirect
from .models import Product


def productIndex(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(
        request=request,
        template_name='product/index.html',
        context=context
    )


def createProduct(request):
    if request.method == "POST":
        # Note: The 'request' object has a queryDict named 'POST' which is sent from the frontend form.
        # Note: That queryDict contains the CSRF-Middleware-Token & the input field values of the form in key-value pairs.
        # (Optional) The values of the queryDict are inside individual lists

        # Retrieve the input values from the POST request & store them into variables
        prodName = request.POST.get('product-name')
        prodQuantity = request.POST.get('product-quantity')
        prodPrice = request.POST.get('product-price')

        # Create new record inside the "Product" table in DB
        Product.objects.create(
            name=prodName,
            quantity=prodQuantity,
            price=prodPrice
        )

        return redirect('product-list')

    return render(
        request=request,
        template_name='product/create-product.html'
    )


def detailProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        # Retrieve the input values from the POST request & store them into variables
        prodName = request.POST.get('product-name')
        prodQuantity = request.POST.get('product-quantity')
        prodPrice = request.POST.get('product-price')

        # Update the detail of the Product instance
        product.name = prodName
        product.quantity = prodQuantity
        product.price = prodPrice

        # Store the instance into the DB
        product.save()

        # Redirect to the "Product-List" page
        return redirect('product-list')
        
    context={'product':product}
    return render(
        request=request,
        template_name='product/detail-product.html',
        context=context
    )

def deleteProduct(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product-list')
        
    context={'product':product}
    return render(
        request=request,
        template_name='product/delete-product.html',
        context=context
    )