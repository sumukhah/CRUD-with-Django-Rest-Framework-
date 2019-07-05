from django.urls import path
from .views import PostListView, PostDetailView, CommentView


urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('detail/<pk>/', PostDetailView.as_view(), name='detail'),
    path('detail/<pk>/comments', CommentView.as_view(), name='comments')
]
