"""URLs to communicate with the APIs of the words app."""
from django.urls import path
from words.views import post_words, WordsDictionaryAPI

urlpatterns = [
    path("", WordsDictionaryAPI.as_view()),
    path("add_words/", post_words),
]
