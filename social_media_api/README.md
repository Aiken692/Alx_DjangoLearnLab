# Social Media API

## Overview
This project is a social media API that allows users to register, login, follow, and unfollow other users. It uses Django and Django REST Framework for the backend, and JWT for authentication.

## Models

### CustomUser
The `CustomUser` model extends Django's `AbstractUser` and includes a many-to-many relationship for following other users.

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

 Migrations
To apply the changes to the user model, run the following commands:

python manage.py makemigrations
python manage.py migrate

API Endpoints
Register
URL: /register/
Method: POST
Payload:

{
  "username": "user",
  "password": "pass",
  "email": "email@example.com"
}

Response:
{
  "refresh": "refresh_token",
    "access": "access_token"
}

Login
URL: /login/
Method: POST
Payload:
{
  "username": "user",
  "password": "pass"
}


Response:
{
  "refresh": "refresh_token",
  "access": "access_token"
}

Follow User
URL: /follow/<user_id>/
Method: POST
Headers: Authorization: Bearer <token>
Response: 204 No Content
Unfollow User
URL: /unfollow/<user_id>/
Method: POST
Headers: Authorization: Bearer <token>
Response: 204 No Content
Views
views.py

from django.shortcuts import get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer, TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not (username and password and email):
            return Response({'error': 'Missing fields'}, status=400)

        user = CustomUser.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=400)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response(status=status.HTTP_204_NO_CONTENT)


URL Configurations
urls.py

from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]

Serializers
serializers.py

from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'following', 'followers']

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token