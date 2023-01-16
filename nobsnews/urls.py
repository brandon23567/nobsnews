from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('not_ready/', views.not_ready, name="not_ready"),
    path('<int:pk>/', views.article_detail, name="article_detail"),
]
