from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin

from .models import Post
from .serializers import PostSerializer


class PostListView(CreateModelMixin, ListAPIView):
   
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('created')
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)
