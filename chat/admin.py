from django.contrib import admin
from .models import Room, Message
# Register your models here.

admin.site.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('first_user','second_user')

    class Meta:
        model = Room

""" admin.site.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'room')

    class Meta:
        model = ChatUser  """

admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'content', 'created_at')

    class Meta:
        model = Message