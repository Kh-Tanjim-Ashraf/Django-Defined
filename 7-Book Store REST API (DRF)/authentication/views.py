from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializer import UserSerializer



class UserAPIView(APIView):

    def post(self, request):
        serialized = UserSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
