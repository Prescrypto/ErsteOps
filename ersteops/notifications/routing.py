#from channels import route
from django.conf.urls import url, re_path
#from .consumers import ws_connect, ws_receive, ws_disconnect
#from .consumers import ErsteConsumer
from django.urls import path

from . import consumers

# websocket_routing = [
#     # Called when WebSockets connect
#     route("websocket.connect", ws_connect),

#     # Called when WebSockets get sent a data frame
#     route("websocket.receive", ws_receive),

#     # Called when WebSockets disconnect
#     route("websocket.disconnect", ws_disconnect),
# ]



# websocket_routing = [
#     # Called when WebSockets connect
#     url("websocket.connect", ws_connect),

#     # Called when WebSockets get sent a data frame
#     url("websocket.receive", ws_receive),

#     # Called when WebSockets disconnect
#     url("websocket.disconnect", ws_disconnect),
# ]

# websocket_urlpatterns = [
#     # Called when WebSockets connect
#     re_path(r"ws/websocket.connect", ws_connect),

#     # Called when WebSockets get sent a data frame
#     re_path(r"ws:websocket.receive", ws_receive),

#     # Called when WebSockets disconnect
#     re_path(r"ws:websocket.disconnect", ws_disconnect),
# ]

websocket_urlpatterns = [
    #re_path(r'notify/emergency/(?P<room_name>\w+)/$', consumers.ErsteConsumer.as_asgi()),
    re_path(r'ws/notify/(?P<room_name>\w+)/$', consumers.ErsteConsumer.as_asgi()),
]