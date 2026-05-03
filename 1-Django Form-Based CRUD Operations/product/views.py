from django.shortcuts import render, redirect
from .models import Product


def productIndex(request):
    context = {}
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

        # Retrive the input values from the POST request & store them into variables
        prodName = request.POST.get('product-name')
        prodQuantity = request.POST.get('product-quantity')
        prodPrice = request.POST.get('product-price')

        # Create new record inside the "Product" table in DB
        Product.objects.create(
            name=prodName,
            quantity=prodQuantity,
            price=prodPrice
        )

        return redirect('create-new-product')

    return render(
        request=request,
        template_name='product/create-product.html'
    )