"""Admin script to connect database to admin view panel."""
from django.contrib import admin

from words.models import WordsDictionary

admin.site.register(WordsDictionary)
