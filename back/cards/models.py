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

# 설문조사
class Survey(models.Model):
    car_owner = models.BooleanField(default=False)
    live_alone = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    baby = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    easy_pay = models.BooleanField(default=False)
    healthcare = models.BooleanField(default=False)
    telecom = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    friends = models.BooleanField(default=False)
    fitness = models.BooleanField(default=False)
    movie = models.BooleanField(default=False)
    travel_inter = models.BooleanField(default=False)
    trevel_dome = models.BooleanField(default=False)
