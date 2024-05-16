from django.urls import path
from . import views

urlpatterns = [
    # 크롤링
    path('card_gorilla_selenium/', views.card_gorilla_selenium),
    # 카드
    path('', views.card_list),
    path('<int:card_pk>/', views.card_detail),
    path('<int:card_pk>/review/', views.review),
    path('<int:card_pk>/review/<int:review_pk>/', views.review),
    path('favorite/', views.favorite),
]
