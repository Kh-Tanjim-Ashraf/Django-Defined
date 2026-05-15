from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from product.models import Product
from product.forms.product_model_form import ProductForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class ProductListView(ListView):
    model = Product
    template_name = 'product/cbv_templates/list-product.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/cbv_templates/detail-product.html'
    context_object_name = 'product'


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    template_name = 'product/cbv_templates/create-product.html'
    form_class = ProductForm
    success_url = reverse_lazy('CBV_PRODUCT:product-list-CBV')
    success_message = "Successfully added a new product!"


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/cbv_templates/update-product.html'
    success_url = reverse_lazy('CBV_PRODUCT:product-list-CBV')
    success_message = "Successfully updated the product!"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/cbv_templates/delete-product.html'
    success_url = reverse_lazy('CBV_PRODUCT:product-list-CBV')

    def get_success_url(self):
        messages.success(self.request, f"{self.object} Product deleted successfully!")
        return super().get_success_url()