from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from product.models import Product
from product.forms.product_model_form import ProductForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'product/cbv_templates/list-product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/cbv_templates/detail-product.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/cbv_templates/create-product.html'
    form_class = ProductForm
    success_url = reverse_lazy('CBV_PRODUCT:product-list-CBV')