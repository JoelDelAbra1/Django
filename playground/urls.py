from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:pk>/', views.room, name="room"),
    path('home/', views.home, name = "home"),
    path('create-room/', views.create_room , name="create-room"),
    path('update-room/<str:pk>/', views.update_room , name="update-room"),
    path('delete-room/<str:pk>/', views.delete_room , name="delete-room")
    ]
