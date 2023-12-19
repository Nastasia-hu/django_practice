"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.
一个基于WSGI的web服务器进入点，提供底层的网络通信功能
For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
