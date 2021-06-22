from channels import include
#from django.conf.urls import include

channel_routing = [
    include("notifications.routing.websocket_routing"),
]
