"""
Is an interface to AnkiConnect.
"""
import json
import urllib.request

from constants import ANKI_CONNECT_URL

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
        print(
            f"URLError: Could not reach: {ANKI_CONNECT_URL}. Make sure that Anki is opened and AnkiConnect is installed."
        )

        return
    response = json.load(response_json)

    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]
