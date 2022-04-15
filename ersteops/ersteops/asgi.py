import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

import notifications.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ersteops.settings')
django.setup()


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
