from django.urls import path
from views.func_based_views_html_forms import productIndex, createProduct, detailProduct, deleteProduct

urlpatterns = [
    # Function-based view with HTML form for CRUD operations
    path('', view=productIndex, name='product-list'),
    path('create-new-product/', view=createProduct, name='create-new-product'),
    path('product-detail/<int:pk>/', view=detailProduct, name='product-detail'),
    path('product-delete/<int:pk>/', view=deleteProduct, name='product-delete'),
]
