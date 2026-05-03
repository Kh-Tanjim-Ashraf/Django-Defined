from django.urls import path
from .views import productIndex, createProduct

urlpatterns = [
    path('', view=productIndex, name='product-list'),
    path('create-new-product/', view=createProduct, name='create-new-product'),
]
