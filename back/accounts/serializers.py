from rest_framework import serializers
from cards.models import Recommendation
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class RecommedationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recommendation
            fields = '__all__'

    recommendations = RecommedationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender', 'recommendations')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'