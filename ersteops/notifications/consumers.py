# -*- coding: utf-8 -*-
import json

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class ErsteConsumer(WebsocketConsumer): 
    def connect(self):
        # print("************************************************************")
        # print("ErsteConsumer.connect")
        # #print(dir(self.scope['url_route']['kwargs']['room_name']))
        # print("************************************************************")
        # print("room_name: {}".format(self.scope['url_route']['kwargs']['room_name']))

        # print("url_route: {}".format(self.scope['url_route']))
        # print("user: {}".format(self.scope['user']))
        # print("path: {}".format(self.scope['path']))
        # print("************************************************************")
        if not self.scope['user'].is_authenticated:
            print("User Not Autenticated")
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name = 'chat_%s' % self.room_name
        #self.room_name = label[2]
        if not self.room_name in ["emergency", "units", "derivation"]:
            print("Invalid Room name or path")
            return

        self.room_group_name = "notifications"
        #print("room_group_name: {}".format(self.room_group_name))

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        #print("************************************************************")
        #print("ErsteConsumer.disconnect")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        #print("************************************************************")
        #print("ErsteConsumer.receive")
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
        # print("************************************************************")
        # print("ErsteConsumer.chat")
        # print("******************************************")
        # print(event)
        # print("******************************************")
        # print(event['message'])
        # print("******************************************")
        # print("group: {}".format(self.room_group_name))
        # print("path: {}".format(self.scope['path']))
        message = event['message']
        message_json = json.dumps(message)
        # print("******************************************")
        # print("realy sending data: {}".format(message_json))

        # Send message to WebSocket
        self.send(text_data = message_json)
        #self.send(text_data=message)
        #self.send_json(event)



