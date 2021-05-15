"""Words app config."""

from django.apps import AppConfig


class WordsConfig(AppConfig):
    """WordsConfig - Application Configuration for Words App."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "words"
