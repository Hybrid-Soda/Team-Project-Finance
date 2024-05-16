from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import *

# 유저 정보 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    if request.user.username == username:
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)