# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
import logging
from .models import Message
from django.contrib.auth.models import User
from django.db import transaction
from channels.db import database_sync_to_async
logger = logging.getLogger(__name__)
'''
метод receive используется для обработки входящих сообщений от клиентов, 
метод chat_message — для обработки сообщений, полученных от других клиентов в рамках одной группы соединений.
'''
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        if isinstance(self.scope['user'], AnonymousUser):
            await self.close()
            logger.debug('Close connect')
        else:
            logger.debug('Connect success')
            self.user = self.scope['user']
            self.room_group_name = f'task_{self.user.id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.channel_layer.group_add('gossip', self.channel_name)
            await self.accept()

    async def connect(self):
        if isinstance(self.scope['user'], AnonymousUser):
            await self.close()
        else:
            self.user = self.scope['user']
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            self.room_group_name = "chat_%s" % self.room_name
            print(self.user)
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)

            await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        


        message_obj = await self.create_chat(message, self.user)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )
    @database_sync_to_async
    def create_chat(self, message, sender):
        return Message.objects.create(user=User(1),recipient=User(2), text=message)
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
      
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,"user":1}))