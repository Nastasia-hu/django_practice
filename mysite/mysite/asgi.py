"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.
一个基于ASGI的web服务器进入点，提供异步的网络通信功能
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
