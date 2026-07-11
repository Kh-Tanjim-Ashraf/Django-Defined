from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authentication.views import UserAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),

    # JWT Auth Token
    path('api/register/', UserAPIView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
