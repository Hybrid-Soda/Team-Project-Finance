from django.db import models
from django.conf import settings


# 카드정보
class Card(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image_url = models.TextField(blank=True)
    annual_fee1 = models.IntegerField(blank=True, null=True)
    annual_fee2 = models.IntegerField(blank=True, null=True)
    record = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30)

# 카드혜택
class Benefit(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

# 카드추천
class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    score = models.FloatField()

# 카드리뷰
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    rating = models.FloatField()
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
