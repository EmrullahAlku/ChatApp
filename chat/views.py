# chat/views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Room, Message

@login_required(login_url="login")
def index(request):
    Profileusername=request.user
    user = User.objects.all().exclude(username=request.user)
    return render(request, "chat/index.html", {"users": user , "username": Profileusername})

@login_required(login_url="login")
def room(request, room_name):
    Profileusername=request.user
    user = User.objects.all().exclude(username=request.user)
    return render(request, "chat/home.html", {"room_name": room_name, "users": user , "username": Profileusername})

""" def home(request):
    return render(request, "chat/home.html") """

def userLogin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "chat/login.html")

@login_required(login_url="login")
def startChat(request, username):
    second_user=User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user, second_user=second_user)

    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user, first_user=second_user) 
        except Room.DoesNotExist:
            room = Room.objects.create(first_user=request.user, second_user=second_user)
    return redirect ('room', room_name=room.id)