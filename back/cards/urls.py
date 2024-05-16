from django.urls import path
from . import views

urlpatterns = [
    # 크롤링
    path('card_gorilla_selenium/', views.card_gorilla_selenium),
]
