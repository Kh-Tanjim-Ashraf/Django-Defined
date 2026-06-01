from django.urls import path
from product.views.class_based_views import ProductList


urlpatterns = [
    path('list/', view=ProductList.as_view(), name='productList-cbv'),
]