# -*- coding: utf-8 -*-
import json

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class ErsteConsumer(WebsocketConsumer): 
    def connect(self):
        if not self.scope['user'].is_authenticated:
            print("User Not Autenticated")
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']

        if not self.room_name in ["emergency", "units", "derivation"]:
            print("Invalid Room name or path")
            return

        self.room_group_name = "notifications"
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        message_json = json.dumps(message)
        self.send(text_data = message_json)
