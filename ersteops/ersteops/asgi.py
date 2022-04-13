# import os
# import channels.asgi

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ersteops.settings")
# channel_layer = channels.asgi.get_channel_layer()

import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
#from channels.routing import get_default_application
#from channels.layers import get_channel_layer
#from django.core.asgi import get_asgi_application

import notifications.routing
#from  notifications import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ersteops.settings')
#import django
django.setup()
#application = get_default_application()

# application = ProtocolTypeRouter({
#   #"http": AsgiHandler(),
#   #"http": get_asgi_application(),
#   # Just HTTP for now. (We can add other protocols later.)
#   "websocket": AuthMiddlewareStack(
#         URLRouter(notifications.routing.websocket_urlpatterns)),


# })

#channel_layer = get_channel_layer()


# from channels import include

# channel_routing = [
#     include("notifications.routing.websocket_routing"),
# ]

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                notifications.routing.websocket_urlpatterns
            )
        )
    ),
})