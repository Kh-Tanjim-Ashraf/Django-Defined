from django.urls import path
from product.views.func_based_views import productList


urlpatterns = [
    path('list/', view=productList, name='productList-fbv'),
]