from django.urls import path
from . import views

urlpatterns = [
    path('', views.post),
    path('<int:post_pk>/', views.post_detail),
    path('<int:post_pk>/likes/', views.post_like),
    path('<int:post_pk>/comments/', views.comment),
    path('<int:post_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path('<int:post_pk>/comments/<int:comment_pk>/like/', views.comment_like),
]
