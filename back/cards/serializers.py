from rest_framework import serializers
from .models import *


class BenefitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    benefit_set = BenefitListSerializer(many=True)
    review_set = ReviewSerializer(many=True)
    class Meta:
        model = Card
        fields = (
            'id', 'name', 'brand', 'image_url', 'annual_fee1',
            'annual_fee2', 'record', 'type', 'benefit_set', 'review_set'
        )