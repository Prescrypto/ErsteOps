from django.shortcuts import render, redirect
from .models import Room


def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    ctx={'room': room, 'messages': messages}
    return render(request, "chat/room.html", ctx)