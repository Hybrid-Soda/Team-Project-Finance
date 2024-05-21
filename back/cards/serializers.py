from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class BenefitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username', 'nickname')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'card')


class CardSerializer(serializers.ModelSerializer):
    benefit_set = BenefitListSerializer(many=True)
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = Card
        fields = (
            'id', 'name', 'brand', 'image_url', 'annual_fee1',
            'annual_fee2', 'record', 'type', 'benefit_set', 'review_set'
        )

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
        read_only_fields = ('user',)