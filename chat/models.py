import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#DM
class Room(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_user = models.ForeignKey(User, verbose_name="First User", related_name='room_first', on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, verbose_name="Second User", related_name='room_second', on_delete=models.CASCADE)

class Message(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, verbose_name="User", related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Room", related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)