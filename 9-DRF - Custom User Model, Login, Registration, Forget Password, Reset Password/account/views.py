from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializer import UserRegistrationSerializer


User = get_user_model()


class UserRegistration(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {'msg': 'User created successfully'}
            
            return Response(data=data, status=status.HTTP_201_CREATED)