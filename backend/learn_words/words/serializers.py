"""Serializers for values stored in database tables related to words app."""
from rest_framework import serializers

from words.models import WordsDictionary


class WordsDictionarySerializer(serializers.ModelSerializer):
    """WordsDictionarySerializer: Serializer for fetching details from db."""

    class Meta:
        """Class to define what metadata needs to be fetched from the db."""

        model = WordsDictionary
        fields = (
            "id",
            "group",
            "word",
            "definition",
            "example_sentences",
            "gre_synonyms",
            "synonyms",
            "antonyms",
        )
