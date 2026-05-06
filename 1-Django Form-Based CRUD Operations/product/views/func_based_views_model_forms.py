from django.shortcuts import render, redirect, get_object_or_404
from product.forms.model_forms import ProductForm
from product.models import Product

# Product List
def productIndex(request):
    products=Product.objects.all()
    context={'products':products}
    return render(
        request=request,
        template_name='product/django_form_based_crud/index.html',
        context=context
    )

[]
# Product Create
def productCreate(request):
    # Post Request
    if request.method == 'POST':
        data = ProductForm(data=request.POST)
        if data.is_valid():
            data.save()
            return redirect('product-list-dj-form')
    
    # Get Request
    form=ProductForm()
    
    context={'form':form}
    
    return render(
        request=request,
        template_name='product/django_form_based_crud/create-product.html',
        context=context
    )


# Product Update
def productUpdate(request, pk):
    product=get_object_or_404(Product, pk=pk)
    
    # Post Request
    if request.method == "POST":
        data=ProductForm(data=request.POST)
        if data.is_valid():
            form = ProductForm(data=request.POST, instance=product) # Pass the data from the frontend form along with the product-object to update the data
            form.save() # Commit the change
            return redirect('product-list-dj-form')

    # Get Request
    form=ProductForm(instance=product) # While rendering the form, pass the obj as 'instance' param to populate the data.

    context={
        'form':form,
        'product':product
    }
    
    return render(
        request=request,
        template_name='product/django_form_based_crud/update-product.html',
        context=context
    )