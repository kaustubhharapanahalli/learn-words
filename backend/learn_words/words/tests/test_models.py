"""Unit testing the functionality of models."""
from typing import List

from django.test import TestCase

from words.models import WordsDictionary

GROUP = "Group 1"
WORD = "abound"
DEFINITIONS = [
    "Exist in large numbers or amounts.",
    "Have in large numbers or amounts.",
]
EXAMPLE_SENTENCES = [
    "Speculation abounds as to how long Amir Khan can turn his back on the long line of promoters beating a path to his door and remain in the amateur ranks.",
    "Deadpan humour abounds and the curmudgeonly Fin has a whole repertoire of exasperated sighs and steely stares as he attempts to bite the hand of friendship.",
    "In some situations, the declines are so gentle that arguments abound as to whether a bear market really existed at all.",
]
SYNONYMS = [
    "superabound",
    "flourish",
]
ANTONYMS = ["be scarce"]
GRE_SYNONYMS = ["proliferate", "thrive"]


class WordsDictionaryTest(TestCase):
    """WordsDictionaryTest: Unit testing of WordsDictionary models."""

    def create_word_dictionary(
        self,
        group: str,
        word: str,
        definition: List[str],
        example_sentences: List[str],
        gre_synonyms: List[str],
        synonyms: List[str],
        antonyms: List[str],
    ) -> WordsDictionary:
        """
        create_word_dictionary: Create a sample object for the db.

        Parameters
        ----------
        group : str, optional
            Name of the group to which the word belongs, by default GROUP.
        word : str, optional
            Word for which the metadata needs to be stored, by default WORD.
        definition : list, optional
            Definition of the word, by default DEFINITIONS.
        example_sentences : list, optional
            Example sentences for the word, by default EXAMPLE_SENTENCES.
        gre_synonyms : list, optional
            GRE synonyms for the word, by default GRE_SYNONYMS.
        synonyms : list, optional
            General Synonyms related to the word, by default SYNONYMS.
        antonyms : list, optional
            Antonyms related to the word, by default ANTONYMS.

        Returns
        -------
        WordsDictionary
            Returns an object of type WordsDictionary
        """
        return WordsDictionary.objects.create(
            group=group,
            word=word,
            definition=definition,
            example_sentences=example_sentences,
            gre_synonyms=gre_synonyms,
            synonyms=synonyms,
            antonyms=antonyms,
        )

    def test_word_dictionary_creation(self):
        """test_word_dictionary_creation: Test creation of a row of data."""
        test_object = self.create_word_dictionary(
            group=GROUP,
            word=WORD,
            definition=DEFINITIONS,
            example_sentences=EXAMPLE_SENTENCES,
            gre_synonyms=GRE_SYNONYMS,
            synonyms=SYNONYMS,
            antonyms=ANTONYMS,
        )
        self.assertTrue(isinstance(test_object, WordsDictionary))
        self.assertTrue(test_object.__str__, WORD)
