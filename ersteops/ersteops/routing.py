from channels import include

channel_routing = [
    #include("minichat.routing.websocket_routing", path=r"^/chat/stream"),
    include("minichat.routing.websocket_routing"),
    #include("minichat.routing.custom_routing")
]
