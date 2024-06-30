from django.conf import settings
from django.http import HttpResponseRedirect

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from django.shortcuts import render
from rest_framework import views, generics, permissions, status
from rest_framework.response import Response

#local imports
from authentication.serializers import  UserSerializer, RegisterSerializer, LoginSerializer

from authentication.exception import ProfileNotFound
# third party imports
from knox.models import AuthToken


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/"
    client_class = OAuth2Client
    


# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        user.save()
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        }, status=status.HTTP_200_OK)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        }, status=status.HTTP_200_OK)

class UserAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = ( 
        permissions.IsAuthenticated,
    )
    def get(self,request):
        user = self.request.user 
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)