"""
WSGI config for Proyect_end project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

## Mi primir hola mundo en el proyecjo jsjsjsjs
##hola frabricio que fue mano no me aparece tu codigo
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyect_end.settings')

application = get_wsgi_application()
