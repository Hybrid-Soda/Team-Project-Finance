from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from cards.models import Recommendation
from cards.models import Card
from .models import *


class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False)
    gender = serializers.CharField(max_length=10)
    age = serializers.IntegerField()

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class RecommedationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recommendation
            fields = '__all__'

    recommendations = RecommedationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender', 'recommendations', 'favorite_cards')

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
        read_only_fields = ('user',)

class UserProfileSerializer(serializers.ModelSerializer):
    # class RecommedationSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Recommendation
    #         fields = '__all__'

    # recommendations = RecommedationSerializer()

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender', 'survey_set')

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender')