from django.urls import path
from product.views import productList


urlpatterns = [
    path('list/', productList, name='productList'),
]
