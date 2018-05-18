# -*- coding: utf-8 -*-
import simplejson as json
from channels import Group
from channels.sessions import channel_session



from channels.auth import channel_session_user_from_http, channel_session_user
from channels import Channel
@channel_session_user_from_http
def ws_connect(message):
    #Cuando se realiza una coneccion, se busca con el path si viene de la url adecuada
    message.reply_channel.send({"accept": True})

    user=message.user

    if not user.is_authenticated():
        print("user no authenticated")
        return
    try:
        prefix, label = message['path'].strip('/').split('/')
        if prefix != 'notify':
            print('invalid ws path=%s'%message['path'])
            return
    except ValueError:
        print('invalid ws path=%s'%message['path'])
        return
    if not label in ["emergency", "units", "derivation"]:
        print('invalid ws path=%s'%message['path'])
        return

    message.channel_session['room'] = label
    Group("notifications", channel_layer=message.channel_layer).add(
            message.reply_channel)


@channel_session
def ws_receive(message):
    print(message['text'])

@channel_session_user
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        Group('notify-'+label, channel_layer=message.channel_layer).discard(
            message.reply_channel)
    except KeyError:
        pass
