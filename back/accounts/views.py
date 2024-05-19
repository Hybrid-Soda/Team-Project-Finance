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

# 유저 정보 조회 / 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    if request.method == "GET":
        if request.user.username == username:
            serializer = UserProfileSerializer(request.user)
            return Response(serializer.data)
    
    if request.method == "PUT":
        if request.user.username == username:
            serializer = EditProfileSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

# 설문 조사 등록 / 수정
@api_view(["POST", "PUT"])
@permission_classes([IsAuthenticated])
def survey(request, username):

    if request.method == "POST":
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        survey = get_object_or_404(get_user, username=username)
        if request.user == survey.user:
            serializer = SurveySerializer(survey, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)