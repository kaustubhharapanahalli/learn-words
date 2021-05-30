"""URLs to communicate with the APIs of the words app."""
from django.urls import path
from words.views import post_words, get_groups, WordsDictionaryAPI

urlpatterns = [
    path("", WordsDictionaryAPI.as_view()),
    path("add_words/", post_words),
    path("get_groups/", get_groups),
]
