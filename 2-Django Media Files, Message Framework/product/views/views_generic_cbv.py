from django.views.generic import ListView
from django.views.generic.detail import DetailView
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/cbv_templates/list-product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/cbv_templates/detail-product.html'
    context_object_name = 'product'