from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from account.views import UserRegistration, UserLogin, UserDetail, UserPasswordUpdate


urlpatterns = [
    # path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/login/', UserLogin.as_view(), name='token_login'),
    path('token/registration/', UserRegistration.as_view(), name='token_registration'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserDetail.as_view(), name='user_detail'),
    path('change-password/', UserPasswordUpdate.as_view(), name='user_password_update'),
]