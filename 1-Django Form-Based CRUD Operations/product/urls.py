from django.urls import path
from .views import productIndex

urlpatterns = [
    path('', view=productIndex, name='product-list'),
]
