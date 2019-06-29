from django.urls import path, include
from .views import GithubLogin, FacebookLogin


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register', include('rest_auth.registration.urls')),
    path('github/',GithubLogin.as_view(), name='github_auth'),
    path('facebook/', FacebookLogin.as_view(), name='github_auth'),
]
