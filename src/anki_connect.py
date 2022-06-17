"""
Is an interface to AnkiConnect.
"""

import json
import urllib.request
import sys

from constants import ANKI_CONNECT_URL, CONNECTION_ERROR_MESSAGE

ANKI_CONNECT_URL = "http://localhost:8765"


def request(action, **params):
    """Returns a request dict to be sent to AnkiConnect."""
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    """Invokes AnkiConnect and returns the response."""
    request_json = json.dumps(request(action, **params)).encode("utf-8")
    try:
        response_json = urllib.request.urlopen(
            urllib.request.Request(ANKI_CONNECT_URL, request_json)
        )
    except urllib.error.URLError:
        print(CONNECTION_ERROR_MESSAGE)
        sys.exit()

    response = json.load(response_json)

    return handle_response(response)


def handle_response(response):
    """Handles the response from AnkiConnect."""
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


# For testing purposes.
if __name__ == "__main__":

    invoke("deckNames")
    # handle_response({"result": None, "error": "unsupported action"})
    # raise Exception("unsupported action")
