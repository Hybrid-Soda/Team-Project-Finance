from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'nickname')

class PostListSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)
        class Meta:
            model = Post
            fields = ('id', 'user', 'like_users', 'content', 'created_at')

    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'like_users')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'post')
