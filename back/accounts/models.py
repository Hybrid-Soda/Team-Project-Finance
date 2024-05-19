from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import AbstractUser
from django.db import models
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

# 설문조사
class Survey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        gender = data.get("gender")
        age = data.get("age")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user.gender = gender
        if age:
            user.age = age
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
            self.populate_username(request, user)
        if commit:
            user.save()
        return user