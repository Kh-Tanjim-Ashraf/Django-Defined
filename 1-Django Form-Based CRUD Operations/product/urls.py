from django.urls import path
from .views import productIndex, createProduct, detailProduct, deleteProduct

urlpatterns = [
    path('', view=productIndex, name='product-list'),
    path('create-new-product/', view=createProduct, name='create-new-product'),
    path('product-detail/<int:pk>/', view=detailProduct, name='product-detail'),
    path('product-delete/<int:pk>/', view=deleteProduct, name='product-delete'),
]
