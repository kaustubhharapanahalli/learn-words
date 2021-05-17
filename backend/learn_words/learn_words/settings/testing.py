"""Settings file for development of application."""
from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "learn_words",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
