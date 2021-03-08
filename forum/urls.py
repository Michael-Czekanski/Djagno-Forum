from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="forum-home"),
    path('about/', views.about, name="forum-about"),
    path('topic/<int:topic_id>/', views.topic, name="forum-topic"),
    path('topic/new/', views.topic_create, name="topic-create"),
]
