from django.conf.urls import url, re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notify/(?P<room_name>\w+)/$', consumers.ErsteConsumer.as_asgi()),
]