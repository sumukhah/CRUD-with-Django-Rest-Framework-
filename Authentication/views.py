from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import RegisterView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


from .permissions import IsOwnerOrReadOnly
from .serializers import CustomRegisterSerializer, UserProfileSerializer
from .models import User


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client


class CustomRegisterView(RegisterView):
    queryset = User.objects.all()
    serializer_class = CustomRegisterSerializer


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ]

    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            User.objects.get(pk=pk)
        except:
            content = {
                'status': 'User Does Not Exist'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return User.objects.all()
