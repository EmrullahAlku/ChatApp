import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    #Websocket bağlantı kurulduğunda çalışır
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    #Websocket bağlantısı kesildiğinde çalışır
    async def disconnect(self , close_code):
        await self.channel.name.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )
    #Websocket mesaj alındığında çalışır
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message , 
            })
    #mesajı client'e gönderir
    async def sendMessage(self , event) : 
        message = event["message"]
        await self.send(text_data = json.dumps({"message":message}))
      