# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("home/", views.home, name="home"),
    path("<str:room_name>/", views.room, name="room"),
    path('start_chat/<str:username>', views.startChat, name='start_chat'),
]