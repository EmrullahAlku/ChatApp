import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    #Websocket, works when connected
    async def connect(self):
        self.roomName = self.scope['url_route']['kwargs']['room_name']
        self.roomGroupName = f"chat_{self.roomName}"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    #Websocket, works when disconnected
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
    #Websocket, works when message is received
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        user = self.scope["user"]
        m=message = await sync_to_async(Message.objects.create)(user=user, content=message_content, room_id=self.roomName)
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message.content ,
                'user' : user.username,
                'created_at' : m.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
    #Websocket, sends the message to the client
    async def sendMessage(self , event) : 
        message = event["message"]
        user=event["user"]
        created_at = event["created_at"]
        await self.send(text_data = json.dumps({"message": message , "user": user, "created_at": created_at}))

      