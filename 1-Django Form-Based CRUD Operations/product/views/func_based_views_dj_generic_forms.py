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
            # Get the variables from the form-inputs
            prodName = form.cleaned_data.get('name')
            prodQuantity = form.cleaned_data.get('quantity')
            prodPrice = form.cleaned_data.get('price')

            # Save to DB
            Product.objects.create(
                name=prodName,
                quantity=prodQuantity,
                price=prodPrice
            )

            return redirect('product-list-dj-gen-form')
    else:
        form=ProductFormGen()        
        
    context={'form':form}
    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/create-product.html',
        context=context
    )


def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    
    if request.method == "POST":
        # Pass the product object as `data` of the form for further validations
        form = ProductFormGen(data=request.POST)
        if form.is_valid():
            # Store the request data
            prodName = form.cleaned_data.get('name')
            prodQuantity = form.cleaned_data.get('quantity')
            prodPrice = form.cleaned_data.get('price')
            print(f"product name: {prodName}; quantity: {prodQuantity}; price: {prodPrice}")

            # Update the value of previously retrieved product object
            product.name = prodName
            product.quantity = prodQuantity
            product.price = prodPrice

            # Save the product object to update the record into the DB
            product.save()

            # After saving the record to DB, redirect the user to the product-list page
            return redirect('product-list-dj-gen-form')
    else:
        # Map the model fields' values to a dictionary for the form
        initial_data = {
            'name': product.name,
            'quantity': product.quantity,
            'price': product.price
        }
        form = ProductFormGen(initial=initial_data) # Instead of 'instance' param for the model-form, for Django standard form, 'initial' param is used to populate the product-record.

    context = {
        'form': form,
        'product':product
    }

    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/update-product.html',
        context=context
    )


def productDelete(request, pk):
    product=Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list-dj-gen-form')
    context={'product':product}
    return render(
        request=request,
        template_name='product/django_generic_form_based_crud/delete-product.html',
        context=context
    )
