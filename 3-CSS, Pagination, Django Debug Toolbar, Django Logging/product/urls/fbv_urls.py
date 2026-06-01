from django.urls import path
from product.views.func_based_views import productList, productCreate, productUpdate, productDelete


urlpatterns = [
    path('list/', view=productList, name='productList-fbv'),
    path('create/', view=productCreate, name='productCreate-fbv'),
    path('update/<int:pk>/', view=productUpdate, name='productUpdate-fbv'),
    path('delete/<int:pk>/', view=productDelete, name='productDelete-fbv'),
]