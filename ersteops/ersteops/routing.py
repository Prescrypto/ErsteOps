from channels import include

channel_routing = [
    #include("notifications.routing.websocket_routing", path=r"^/notification/dashboard"),
    include("notifications.routing.websocket_routing"),
]
