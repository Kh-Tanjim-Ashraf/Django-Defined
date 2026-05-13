from django.urls import path
from product.views.views_fbv import productList, productCreate, productUpdate, productDelete

app_name = 'FBV_Product'

urlpatterns = [
    # Function-based Views
    path('list/', view=productList, name='product-list-FBV'),
    path('create/', view=productCreate, name='product-create-FBV'),
    path('update/<int:pk>/', view=productUpdate, name='product-update-FBV'),
    path('delete/<int:pk>/', view=productDelete, name='product-delete-FBV'),
]