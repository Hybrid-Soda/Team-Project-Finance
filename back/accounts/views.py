# rest_framework module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import *
from .models import *


get_user = get_user_model()

# 유저 정보 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    if request.user.username == username:
        user = get_object_or_404(get_user, username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

# 설문 조사 등록 / 수정
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def survey(request, username):

    if request.method == "POST":
        serializer = SurveySerializer(Survey, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        survey = get_object_or_404(get_user, username=username)
        if request.user == survey.user:
            serializer = SurveySerializer(Survey, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)