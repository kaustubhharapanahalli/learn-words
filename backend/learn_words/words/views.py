"""Views functionality for Defining APIs."""
from typing import Any, List, Union
import json
import logging

from django.utils.datastructures import MultiValueDict, MultiValueDictKeyError
from django.http import HttpResponseBadRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from errors.file_format_error import FileFormatError
from words.models import WordsDictionary
from words.serializers import WordsDictionarySerializer


@api_view(["POST"])
def post_words(request: Request) -> Union[Response, HttpResponseBadRequest]:
    """
    post_words: Function to save words metadata to database.

    Save metadata of words to database. This function allows users to send a
    POST request only when the user accessing the API is an Administrator.

    Parameters
    ----------
    request : Request
        Request body received from the frontend.

    Returns
    -------
    Union[Response, HttpResponseBadRequest]:
        Custom message saying words have been saved to database. If there is
        any error, HttpResponseBadRequest is raised.

    Raises
    ------
    MultiValueDictKeyError:
        Raised when no file data is provided in the POST call.
    FileFormatError:
        When the format of the file is not JSON, this error is raised.
    """
    try:
        request_file: Any = request.FILES
        if isinstance(request.FILES, MultiValueDict):
            try:
                request_file = request.FILES["file"]
                file_name: str = request_file.name
            except MultiValueDictKeyError as err:
                raise MultiValueDictKeyError("Did not receive a file data")

            ext = file_name.split(".")[-1]

            if not file_name.endswith(".json"):
                raise FileFormatError(
                    f"File format given: .{ext},\nSupported File format: .json"
                )

        word_dict = json.loads(request_file.read())

        all_meaning: List = list()
        for group, _ in word_dict.items():
            for word, _ in word_dict[group].items():
                print(word)
                logging.info(f"Saving metadata of word: {word}")
                all_meaning.append(
                    WordsDictionary(
                        group=group,
                        word=word,
                        definition=word_dict[group][word]["definition"],
                        example_sentences=word_dict[group][word][
                            "example_sentences"
                        ],
                        gre_synonyms=word_dict[group][word]["gre_synonyms"],
                        synonyms=word_dict[group][word]["synonyms"],
                        antonyms=word_dict[group][word]["antonyms"],
                    )
                )

        WordsDictionary.objects.bulk_create(all_meaning)

        return Response({"message": "Saved words to database."})

    except FileFormatError as err:
        return HttpResponseBadRequest(err, status=406)

    except MultiValueDictKeyError as err:
        return HttpResponseBadRequest(err, status=406)


class WordsDictionaryAPI(APIView):
    """WordsDictionaryAPI: API to communicate with WordsDictionary database."""

    def get(self, request: Request) -> Union[Response, HttpResponseBadRequest]:
        """
        Get meaning of all words for the requested words group.

        Parameters
        ----------
        request : Request
            Request body received from the frontend.

        Returns
        -------
        Union[Response, HttpResponseBadRequest]
            Dictionary of serialized words belonging to a group. If the group
            is not found in the database returns HttpResponseBadRequest.
        """
        group_dict: Any = request.data
        group = group_dict["group"]
        words = WordsDictionary.objects.filter(group=group)
        print(words)
        words_serialized: WordsDictionarySerializer
        if words.exists():
            words_serialized = WordsDictionarySerializer(words, many=True)
        else:
            return HttpResponseBadRequest("Word group not found.", status=406)

        return Response(words_serialized.data)
