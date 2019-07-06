from rest_framework import serializers
from .models import Post, Comment
from django.db.models import Count


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'description', 'creator', 'id', 'created',]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    post = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'post', 'comment_text', 'created', 'id', )
