"""Settings file for development of application."""
import os
from pathlib import Path

from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
