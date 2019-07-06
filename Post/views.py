from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .pagination import CustomPagination
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListView(CreateModelMixin, ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        try:
            return Post.objects.all().order_by('created')
        except Post.DoesNotExist:
            content = {
                'status': 'Model has no objects'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        try:
            Post.objects.get(pk=self.kwargs['pk'])
        except:
            content = {
                'status': 'Post Does Not Exist'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Post.objects.all()


class CommentView(CreateModelMixin, ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        post_pk = self.kwargs['pk']
        return Comment.objects.filter(post=post_pk).order_by('created')

    def perform_create(self, serializer):
        post_pk = self.kwargs['pk']
        post = Post.objects.get(id=post_pk)
        serializer.save(user=self.request.user, post=post)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response('')
