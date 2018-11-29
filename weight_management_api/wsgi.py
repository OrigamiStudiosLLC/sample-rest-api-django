"""
WSGI config for weight_management_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weight_management_api.config.local')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

application = get_wsgi_application()
