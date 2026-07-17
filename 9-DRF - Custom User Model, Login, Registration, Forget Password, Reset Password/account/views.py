from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate


User = get_user_model()


class UserRegistration(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {'msg': 'User created successfully'}
            
            return Response(data=data, status=status.HTTP_201_CREATED)



class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                data = {'msg': 'Login successful'}
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data = {'msg': 'Email or password is invalid'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)
                