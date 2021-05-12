"""
WSGI config for learn_words project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "learn_words.settings.{}".format(
        os.environ.get("DJANGO_CONFIGURATION", "development")
    ),
)

application = get_wsgi_application()
