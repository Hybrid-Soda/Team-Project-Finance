from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.UserProfileView.as_view(), name='userProfile'),
    path('<str:username>/survey/', views.survey),
]
