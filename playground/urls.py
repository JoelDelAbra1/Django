from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:pk>/', views.room, name="room"),
    path('home/', views.home)
    ]
