from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet

router = DefaultRouter()
router.register(r'books', viewset=BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]