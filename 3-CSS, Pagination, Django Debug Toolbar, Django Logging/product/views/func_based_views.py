from django.shortcuts import render, redirect
from product.models import Product
from django.core.paginator import Paginator
from django.db import connection
from product.forms.product_model_form import ProductForm


def productList(request):
    products = Product.objects.all().order_by('-id') # Best practise for showcasing paginated data; avoids "Unordered Query Odering"
    paginator = Paginator(products, 10) # Display 5 products each page
    page_num = request.GET.get('page')
    paginated_prods = paginator.get_page(page_num)
    
    # Forcefully invoke the queryset to view the raw SQL query containing Offset & Limit
    list(paginated_prods)

    for query in connection.queries:
        print()
        print(query['sql'])
        print()
    
    context = {
        'title': 'Product List | FBV',
        'paginated_prods':paginated_prods
    }
    return render(
        request=request,
        template_name='./product/fbv/product-list.html',
        context=context
    )


def productCreate(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProductApplication:productList-fbv')
    
    context = {
        'form': form
    }
    return render(
        request=request,
        template_name='./product/fbv/product-create.html',
        context=context
    )


def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ProductApplication:productList-fbv')
    
    context = {
        'form': form,
        'product': product
    }
    return render(
        request=request,
        template_name='./product/fbv/product-update.html',
        context=context
    )


def productDelete(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('ProductApplication:productList-fbv')

    context = {
        'product': product
    }
    return render(
        request=request,
        template_name='./product/fbv/product-delete.html',
        context=context
    )