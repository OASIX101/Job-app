"""
WSGI config for job_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_app.settings.production')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
