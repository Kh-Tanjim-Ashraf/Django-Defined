from django.shortcuts import render
from rest_framework import viewsets
from book.models import Book
from book.serializer import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]