from django.urls import path
from product.views.views_generic_cbv import ProductListView

app_name = 'CBV_Product'

urlpatterns = [
    path('list/', view=ProductListView.as_view(), name='product-list-CBV'),
]