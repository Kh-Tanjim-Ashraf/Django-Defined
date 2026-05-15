from django.urls import path
from product.views.views_generic_cbv import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'CBV_Product'

urlpatterns = [
    path('list/', view=ProductListView.as_view(), name='product-list-CBV'),
    path('create/', view=ProductCreateView.as_view(), name='product-create-CBV'),
    path('detail/<int:pk>/', view=ProductDetailView.as_view(), name='product-detail-CBV'),
    path('detail/update/<int:pk>/', view=ProductUpdateView.as_view(), name='product-update-CBV'),
    path('delete/<int:pk>/', view=ProductDeleteView.as_view(), name='product-delete-CBV'),
]