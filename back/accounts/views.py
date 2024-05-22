# rest_framework module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import redirect, get_object_or_404
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        user = get_object_or_404(get_user, username=username)
        survey = get_object_or_404(Survey, user=user)
        if request.user == survey.user:
            serializer = SurveySerializer(survey, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
from rest_framework import generics
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

@api_view(["GET"])
def favorite(request, username):
    user = get_object_or_404(get_user, username=username)

    if request.method == "GET":
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    

# @api_view(["GET"])
# def kakaoSignIn(request):
#     app_key = ''
#     redirect_url = 'http://localhost:8000/users/signin/kakao/callback'
#     kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
#     return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_url={redirect_url}')