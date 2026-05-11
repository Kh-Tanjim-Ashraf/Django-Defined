from django.urls import path
from .views import productList, productCreate, productUpdate, productDelete

urlpatterns = [
    # Function-based Views
    path('', view=productList, name='product-list-FBV'),
    path('create/', view=productCreate, name='product-create-FBV'),
    path('update/<int:pk>/', view=productUpdate, name='product-update-FBV'),
    path('delete/<int:pk>/', view=productDelete, name='product-delete-FBV'),
]
