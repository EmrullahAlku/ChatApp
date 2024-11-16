from django.contrib import admin
from .models import Room, Message, ChatUser
# Register your models here.

admin.site.register(Room)

admin.register(Room)
class RommAdmin(admin.ModelAdmin):
    list_display = ('first_user','second_user')

    class Meta:
        model = Room

admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')

    class Meta:
        model = ChatUser 

admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'created_at')

    class Meta:
        model = Message