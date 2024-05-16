from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile),
    path('<str:username>/survey/', views.survey),
]
