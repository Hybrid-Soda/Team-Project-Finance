from django.db import models
from django.contrib.auth.models import AbstractUser
from cards.models import *


class User(AbstractUser):
    # user informations
    favorite_cards = models.ManyToManyField(Card, related_name='favorite_users')
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)