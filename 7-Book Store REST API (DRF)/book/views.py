from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book
from book.serializer import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle



class LargeSetPagination(PageNumberPagination):
    page_size = 5



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Unauthenticated user can only read book record(s); On contrast, authenticated user is allowed to create, update & delete record
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LargeSetPagination
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        q_params = self.request.query_params

        # Order by Price
        order_by_price = q_params.get('ordering')
        queryset = Book.objects.all().order_by(order_by_price if order_by_price else 'id')  # Order by price if provided, otherwise order by `id` column in ascending order

        # Filter by Author
        if q_params.get('author'):
            query = q_params.get('author')
            queryset = queryset.filter(Q(author__icontains=query))

        # Search by Title
        if q_params.get('search'):
            query = q_params.get('search')
            queryset = queryset.filter(Q(title__icontains=query))

        return queryset