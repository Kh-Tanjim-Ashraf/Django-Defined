from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book
from book.serializer import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        # Order by Price
        order_by_price = self.request.query_params.get('ordering')
        print(order_by_price)
        queryset = Book.objects.all().order_by(order_by_price if order_by_price else 'id')

        # Filter by Author
        if self.request.query_params.get('author'):
            query = self.request.query_params.get('author')
            queryset = queryset.filter(Q(author__icontains=query))

        # Search by Title
        if self.request.query_params.get('search'):
            query = self.request.query_params.get('search')
            queryset = queryset.filter(Q(title__icontains=query))

        return queryset