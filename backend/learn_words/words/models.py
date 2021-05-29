"""Define models (database tables) for storing words."""
from django.db import models


class WordsDictionary(models.Model):
    """WordsDictionary: Database table to save words in groups."""

    group = models.CharField(max_length=10, default=None)
    word = models.CharField(
        max_length=50, unique=True, blank=False, null=False
    )
    definition = models.JSONField()
    example_sentences = models.JSONField(default=dict)
    gre_synonyms = models.JSONField()
    synonyms = models.JSONField()
    antonyms = models.JSONField()

    def __str__(self) -> str:
        """
        __str__: String representation of each entry.

        Returns
        -------
        str
            Word name for the row.
        """
        return self.word

    class Meta:
        """Meta class to define Verbose names of the Model."""

        ordering = ["group", "word"]
        verbose_name = "Words Dictionary"
        verbose_name_plural = "Words Dictionary"
