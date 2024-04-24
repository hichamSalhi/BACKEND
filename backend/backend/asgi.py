"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from sensor.consumers import DataConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
print("Starting ASGI application...")

websocket_urlpatterns = [
    path('ws', DataConsumer.as_asgi()),
    # Define other WebSocket URL patterns here... ws://localhost:8000/ws
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
