from django.urls import path
from product.views.views_generic_cbv import ProductListView, ProductDetailView

app_name = 'CBV_Product'

urlpatterns = [
    path('list/', view=ProductListView.as_view(), name='product-list-CBV'),
    path('list/<int:pk>/', view=ProductDetailView.as_view(), name='product-detail-CBV'),
]