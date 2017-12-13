from channels import include

channel_routing = [
    include("notifications.routing.websocket_routing"),
]
