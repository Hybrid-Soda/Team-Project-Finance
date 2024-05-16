from rest_framework import serializers
from .models import *


class BenefitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'brand', 'image_url')

class CardSerializer(serializers.ModelSerializer):
    benefit_set = BenefitListSerializer(many=True)
    review_set = ReviewListSerializer(many=True)

    class Meta:
        model = Card
        fields = (
            'name', 'brand', 'image_url', 'annual_fee1',
            'annual_fee2', 'record', 'type', 'benefit_set'
        )

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'