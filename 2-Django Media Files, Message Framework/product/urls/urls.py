from django.urls import path, include
from product.views.views import Route_To_FBV_Or_CBV_Product

urlpatterns = [
    path('', Route_To_FBV_Or_CBV_Product.as_view(), name='Route_To_FBV_Or_CBV_Product'),
    # Function-based Views
    path('fbv/', include(('product.urls.urls_fbv', 'app_name'), namespace='FBV_PRODUCT')),
]
