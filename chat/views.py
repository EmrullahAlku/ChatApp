# chat/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from chat.forms import RegisterForm
from .models import Room, Message
from django.contrib.auth import logout

@login_required(login_url="login")
def index(request):
    Profileusername=request.user
    user = User.objects.all().exclude(username=request.user)
    return render(request, "chat/index.html", {"users": user , "username": Profileusername})

@login_required(login_url="login")
def room(request, room_name):
    Profileusername=request.user
    room = Room.objects.get(id=room_name)
    first_user = Room.objects.get(id=room_name).first_user
    second_user = Room.objects.get(id=room_name).second_user
    user = User.objects.all().exclude(username=request.user)
    messages = Message.objects.filter(room=room_name)
    
    context = { "first_user" : first_user, 
                "second_user" : second_user,
                "room_name": room.id , 
                "users": user , 
                "username": Profileusername,
                "messages": messages,}
    return render(request, "chat/home.html", context )


def userLogin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, "chat/login.html")


def userLogout(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def delete_account(request):
    user = request.user
    user.delete()
    logout(request)
    messages.success(request, "Your account has been deleted successfully.")
    return redirect("login")

@login_required(login_url="login")
def delete_room_messages(request, room_name):
    room = get_object_or_404(Room, id=room_name)
    print("oda id:" + room_name)
    Message.objects.filter(room=room).delete()
    messages.success(request, "All messages in the room have been deleted.")
    return redirect("room", room_name=room.id)

def userRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Hesabınız Oluşturuldu")
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, "Kullanıcı doğrulaması başarısız oldu.")
                return HttpResponseRedirect('/register')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/register')

    form = RegisterForm
    context = {"form": form}
    return render(request, "chat/register.html", context)

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

@login_required(login_url="login")
def search_messages(request):
    query = request.GET.get('q')
    if query:
        messages = Message.objects.filter(content__icontains=query).select_related('room')
    else:
        messages = Message.objects.none()
    return render(request, "chat/search_results.html", {"messages": messages, "query": query})