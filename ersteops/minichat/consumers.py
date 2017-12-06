import json
from channels import Group
from channels.sessions import channel_session



from channels.auth import channel_session_user_from_http, channel_session_user
from .models import Room
from channels import Channel
# This decorator copies the user from the HTTP session (only available in
# websocket.connect or http.request messages) to the channel session (available
# in all consumers with the same reply_channel, so all three here)
@channel_session_user_from_http
def ws_connect(message):
    #Cuando se realiza una coneccion, se busca con el path si viene de la url adecuada
    #si es el formato de una sala de chat, se busca si existe el modelo con ese label
    message.reply_channel.send({"accept": True})
    message.channel_session['rooms'] = []
    try:
        prefix, label = message['path'].strip('/').split('/')
        if prefix != 'chat':
            print('invalid ws path=%s'%message['path'])
            return
        room = Room.objects.get(label=label)
        print("Sala identificada:")
        print(room)
    except ValueError:
        print('invalid ws path=%s'%message['path'])
        return
    except Room.DoesNotExist:
        print('ws room does not exist label=%s'%label)
        return

    #si existe asigna una variable "room" para recordar facilmente de que room viene
    message.channel_session['room'] = room.label

    #al final la coneccion es agregada a un grupo con el nombre de la sala, todos los
    #que entren a la misma pagina son aregados a este grupo, de esta forma, cuando
    #se replican mensajes, llegaran a todas las conecciones del mismo grupo
    Group('chat-'+label, channel_layer=message.channel_layer).add(message.reply_channel)


@channel_session
def ws_receive(message):
    print("*********mensaje resivido*******")
    print(message['text'])
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        return
    except Room.DoesNotExist:
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        return
    
    if set(data.keys()) != set(('handle', 'message')):
        return

    if data:
        m = room.messages.create(**data)

        # Este es el punto donde se manda el mensaje a todos las conecciones
        #agregadas anteriormente
        Group('chat-'+label, channel_layer=message.channel_layer).send(
            {'text': json.dumps(m.as_dict())})

@channel_session_user
def ws_disconnect(message):
    #cuando la coneccion se termina o desconecta, esta señal elimina la coneccion del
    #Grupo, siempre que existiera una relacion con alguno
    print("Cerrando la coneccion")
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('chat-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)
        print("Se descarto por completo")
    except (KeyError, Room.DoesNotExist):
        print("no se pudo descartar")
        pass



'''

# Channel_session_user loads the user out from the channel session and presents
# it as message.user. There's also a http_session_user if you want to do this on
# a low-level HTTP handler, or just channel_session if all you want is the
# message.channel_session object without the auth fetching overhead.
def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated():
        print("USER_HAS_TO_LOGIN")
    # Find the room they requested (by ID)
    try:
        room = Room2.objects.get(pk=room_id)
    except Room2.DoesNotExist:
        print("ROOM_INVALID")
    # Check permissions
    if room.staff_only and not user.is_staff:
        print("ROOM_ACCESS_DENIED")
    return room

@channel_session_user
def chat_join(message):
    # Find the room they requested (by ID) and add ourselves to the send group
    # Note that, because of channel_session_user, we have a message.user
    # object that works just like request.user would. Security!
    room = get_room_or_error(message["room"], message.user)

    # Send a "enter message" to the room if available
    if True:
        room.send_message("enter message", message.user)

    # OK, add them in. The websocket_group is what we'll send messages
    # to so that everyone in the chat room gets them.
    room.websocket_group.add(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).union([room.id]))
    # Send a message back that will prompt them to open the room
    # Done server-side so that we could, for example, make people
    # join rooms automatically.
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(room.id),
            "title": room.title,
        }),
    })

@channel_session_user
def chat_leave(message):
    # Reverse of join - remove them from everything.
    room = get_room_or_error(message["room"], message.user)

    # Send a "leave message" to the room if available
    if True:
        room.send_message("leave message", message.user)

    room.websocket_group.discard(message.reply_channel)
    message.channel_session['rooms'] = list(set(message.channel_session['rooms']).difference([room.id]))
    # Send a message back that will prompt them to close the room
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(room.id),
        }),
    })

@channel_session_user
def chat_send(message):
    if int(message['room']) not in message.channel_session['rooms']:
        print("ROOM_ACCESS_DENIED")
    room = get_room_or_error(message["room"], message.user)
    room.send_message(message["message"], message.user)
'''