# rest_framework module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *


# 글 전체 조회 / 생성
@api_view(["GET", "POST"])
def post(request):

    if request.method == "GET":
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if request.user.is_authenticated:
            serializer = PostCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# 글 상세 조회 / 수정 / 삭제
@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if request.method == "GET":
        serializer = PostListSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        if request.user == post.user:
            serializer = PostListSerializer(post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == "DELETE":
        if request.user == post.user:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# 글 좋아요
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return Response(context, status=status.HTTP_200_OK)

# 댓글 전체 조회 / 생성
@api_view(["GET", "POST"])
def comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if request.method == "GET":
        comments = post.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(post=post, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# 댓글 수정 / 삭제
@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def comment_detail(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == "PUT":
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == "DELETE":
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# 댓글 좋아요
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment_like(request, post_pk, comment_pk):
    comment = get_object_or_404(Post, pk=comment_pk)
    
    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return Response(context, status=status.HTTP_200_OK)
