from django.urls import path
from product.views.func_based_views_html_forms import \
    productIndex as prodIndx_htmlf, \
    createProduct as createProd_htmlf, \
    detailProduct as detailProd_htmlf, \
    deleteProduct as deleteProd_htmlf
from product.views.func_based_views_model_forms import \
    productIndex as prodIndx_djf, \
    productCreate as prodCreate_djf

urlpatterns = [
    # Function-based view with HTML form for CRUD operations
    path('html-forms/', view=prodIndx_htmlf, name='product-list-html-form'),
    path('html-forms/create-new-product/', view=createProd_htmlf, name='create-new-product-html-form'),
    path('html-forms/product-detail/<int:pk>/', view=detailProd_htmlf, name='product-detail-html-form'),
    path('html-forms/product-delete/<int:pk>/', view=deleteProd_htmlf, name='product-delete-html-form'),
    # Function-based view with Django form for CRUD operations
    path('django-forms/', view=prodIndx_djf, name='product-list-dj-form'),
    path('django-forms/create-new-product/', view=prodCreate_djf, name='create-new-product-dj-form'),
]
