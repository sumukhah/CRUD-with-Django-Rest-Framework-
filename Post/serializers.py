from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'description', 'creator', 'created'] 
        
