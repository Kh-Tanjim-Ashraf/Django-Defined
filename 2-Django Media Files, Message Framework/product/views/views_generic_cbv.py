from django.views.generic import ListView
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/cbv_templates/list-product.html'
    context_object_name = 'products'