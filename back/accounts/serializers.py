from rest_framework import serializers
from .models import User
from cards.models import Recommendation


class UserProfileSerializer(serializers.ModelSerializer):
    class RecommedationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recommendation
            fields = '__all__'

    recommendations = RecommedationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'age', 'gender', 'recommendations')