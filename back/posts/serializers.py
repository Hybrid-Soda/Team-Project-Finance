from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'nickname')

class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('user', 'like_users', 'content', 'created_at')

    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'image', 'created_at', 'updated_at', 'like_users', 'comment_set')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('post',)
