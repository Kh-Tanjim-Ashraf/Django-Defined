from django.shortcuts import render, redirect
from product.models import Product, Stock
from django.core.paginator import Paginator
from django.db import connection
from product.forms.product_model_form import ProductForm


def productList(request):
    # products = Product.objects.all().order_by('-id')

    # Query Optimization: Lately added "select_related" to fetch all the related objects by using single DB query utilizing SQL "JOIN"
    products = Product.objects.select_related('category', 'stock').all().order_by('-id') # Must use "order_by()"; Best practise for showcasing paginated data; avoids "Unordered Query Odering"
    
    # Pagination
    paginator = Paginator(products, 10) # Display 5 products each page
    page_num = request.GET.get('page')
    paginated_prods = paginator.get_page(page_num)
    
    # Forcefully invoke the queryset to view the raw SQL query containing Offset & Limit
    # list(paginated_prods)

    # for query in connection.queries:
    #     print()
    #     print(query['sql'])
    #     print()
    
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
            # form.save()

            """
            **Debug Process**: How to get the newly created product object, because that is required to create a 1-To-1 record into the 'Stock' table
            new_product = form.save(commit=False)
            print(f"New created product: {new_product}")
            print(f"Quantity: {form.cleaned_data.get('quantity')}")
            """
            new_product = form.save()   # Stores the newly created object, since it's required for creating a record in the `Stock` table.

            # Create a 1-To-1 record in the 'Stock' table
            Stock.objects.get_or_create(
                product_id = new_product,
                quantity = form.cleaned_data.get('quantity')
            )

            return redirect('ProductApplication:productList-fbv')
    
    context = {
        'title': 'Create Product | FBV',
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
        'title': f'Update Product | {product.name} | FBV',
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
        'title': f'Delete Product | {product.name} | FBV',
        'product': product
    }
    return render(
        request=request,
        template_name='./product/fbv/product-delete.html',
        context=context
    )