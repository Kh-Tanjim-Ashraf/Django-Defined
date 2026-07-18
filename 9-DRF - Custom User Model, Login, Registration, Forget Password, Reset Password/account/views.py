from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserDetailSerializer, 
    UserPasswordUpdateSerializer,
    UserForgetPassowrdSerializer,
    UserPasswordResetTokenValidationSerializer
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated



User = get_user_model()



def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserRegistration(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # Required to generate JWT token for a newly registered user since s/he will be automatically redirected to the dashboard/any page where authenticated access is required
            data = {
                'message': 'User created successfully',
                'token': get_tokens_for_user(user)
            }
            
            return Response(data=data, status=status.HTTP_201_CREATED)



class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                data = {
                    'message': 'Login successful',
                    'token': get_tokens_for_user(user)
                }
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data = {'message': 'Email or password is invalid'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)



class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(instance=request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)



class UserPasswordUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserPasswordUpdateSerializer(
            data=request.data, 
            context={'user': request.user}
        )

        if serializer.is_valid(raise_exception=True):
            data = {'message': 'Password updated'}

            return Response(data=data, status=status.HTTP_200_OK)



class UserForgetPassowrd(APIView):
    # TODO: Throttling required for the anon users

    def post(self, request):
        serializer = UserForgetPassowrdSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = {'message': 'A password reset link is send to you email address. Please check your inbox or spam'}
            return Response(data=data, status=status.HTTP_200_OK)



class UserPasswordReset(APIView):

    # Select different serializer based on method requests
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserPasswordResetTokenValidationSerializer

    # For validating token; Response immediately if invalid so that the frontend can show this error message beforehand rather than showing that after submitting the password & confirm passwords into `POST` request
    def get(self, request, uid, token):
        serializer = self.get_serializer_class()(data={'uid': uid, 'token': token})

        if serializer.is_valid(raise_exception=True):
            data = {'message': 'Token is valid. Proceed to reset password'}
            return Response(data=data, status=status.HTTP_200_OK)

    # Still validates token, but updates the user password this time 
    def post(self, request, uid, token):
        pass