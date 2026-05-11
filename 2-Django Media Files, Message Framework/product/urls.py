from django.urls import path
from .views import productList

urlpatterns = [
    # Function-based Views
    path('', view=productList, name='product-list-FBV'),
]
