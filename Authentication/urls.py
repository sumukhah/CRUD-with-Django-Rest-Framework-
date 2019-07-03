from django.urls import path, include
from .views import GithubLogin, FacebookLogin, CustomRegisterView, UserProfileView


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register', CustomRegisterView.as_view()),
    path('github/',GithubLogin.as_view(), name='github_auth'),
    path('facebook/', FacebookLogin.as_view(), name='github_auth'),
    path('user/<pk>', UserProfileView.as_view()),
    # path('user/<pk>/profile/list', UserProfileListView.as_view())

]
