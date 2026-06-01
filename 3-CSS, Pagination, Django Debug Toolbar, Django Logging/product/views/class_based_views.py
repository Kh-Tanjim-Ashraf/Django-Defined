from django.views.generic.list import ListView
from product.models import Product


class ProductList(ListView):
    model = Product
    template_name = './product/cbv/product-list.html'