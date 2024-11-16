"""
WSGI config for ChatApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from ChatApp import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.__name__)

application = get_wsgi_application()

