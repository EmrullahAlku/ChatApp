from django.contrib import admin
from .models import Room, Message

admin.site.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('first_user','second_user')

    class Meta:
        model = Room

admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'room','content', 'created_at')

    class Meta:
        model = Message