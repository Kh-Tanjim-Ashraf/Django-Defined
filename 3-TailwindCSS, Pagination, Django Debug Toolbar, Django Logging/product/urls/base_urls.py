from django.urls import path, include

app_name = 'productApp'

urlpatterns = [
    path('fbv/', include('product.urls.fbv_urls')),
    path('cbv/', include('product.urls.cbv_urls')),
]
