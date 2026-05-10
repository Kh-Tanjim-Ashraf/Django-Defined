from django.urls import path
# HTML-based-forms related views
from product.views.func_based_views_html_forms import \
    productIndex as prodIndx_htmlf, \
    createProduct as createProd_htmlf, \
    detailProduct as detailProd_htmlf, \
    deleteProduct as deleteProd_htmlf
# Django-model-based-forms related views
from product.views.func_based_views_model_forms import \
    productIndex as prodIndx_djf, \
    productCreate as prodCreate_djf, \
    productUpdate as prodUpdate_djf, \
    productDelete as prodDelete_djf
# Django-generic-form related views
from product.views.func_based_views_dj_generic_forms import \
    productIndex as prodIndx_dj_genf, \
    productCreate as prodCreate_dj_genf, \
    productUpdate as prodUpdate_dj_genf

urlpatterns = [
    # Function-based view with HTML form for CRUD operations
    path('html-forms/', view=prodIndx_htmlf, name='product-list-html-form'),
    path('html-forms/create-new-product/', view=createProd_htmlf, name='create-new-product-html-form'),
    path('html-forms/product-detail/<int:pk>/', view=detailProd_htmlf, name='product-detail-html-form'),
    path('html-forms/product-delete/<int:pk>/', view=deleteProd_htmlf, name='product-delete-html-form'),

    # Function-based view with Django model-based form for CRUD operations
    path('django-forms/', view=prodIndx_djf, name='product-list-dj-form'),
    path('django-forms/create-new-product/', view=prodCreate_djf, name='create-new-product-dj-form'),
    path('django-forms/update-product/<int:pk>/', view=prodUpdate_djf, name='update-product-dj-form'),
    path('django-forms/delete-product/<int:pk>/', view=prodDelete_djf, name='delete-product-dj-form'),

    # Function-based view with Django generic form for CRUD operations
    path('django-generic-forms/', view=prodIndx_dj_genf, name='product-list-dj-gen-form'),
    path('django-generic-forms/create-new-product', view=prodCreate_dj_genf, name='create-new-product-dj-gen-form'),
    path('django-generic-forms/update-product/<int:pk>/', view=prodUpdate_dj_genf, name='update-product-dj-gen-form'),
]
