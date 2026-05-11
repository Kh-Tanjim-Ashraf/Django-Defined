from django.urls import path
from .views import productList, productCreate

urlpatterns = [
    # Function-based Views
    path('', view=productList, name='product-list-FBV'),
    path('create/', view=productCreate, name='product-create-FBV'),
]
