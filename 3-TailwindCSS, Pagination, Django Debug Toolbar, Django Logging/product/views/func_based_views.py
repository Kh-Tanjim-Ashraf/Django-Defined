from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator
from django.db import connection


def productList(request):
    products = Product.objects.all().order_by('id') # Best practise for showcasing paginated data; avoids "Unordered Query Odering"
    paginator = Paginator(products, 10) # Display 5 products each page
    page_num = request.GET.get('page')
    paginated_prods = paginator.get_page(page_num)
    
    # Forcefully invoke the queryset to view the raw SQL query containing Offset & Limit
    list(paginated_prods)

    for query in connection.queries:
        print()
        print(query['sql'])
        print()
    
    context = {'paginated_prods':paginated_prods}
    return render(
        request=request,
        template_name='./product/fbv/product-list.html',
        context=context
    )
