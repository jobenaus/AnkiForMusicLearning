import json
import urllib.request


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    url = "http://localhost:8765"
    request_json = json.dumps(request(action, **params)).encode("utf-8")
    try:
        response_json = urllib.request.urlopen(
            urllib.request.Request(url, request_json)
        )
    except urllib.error.URLError:
        print(
            f"URLError: Could not reach: {url}. Make sure that Anki is opened and AnkiConnect is installed."
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


invoke("createDeck", deck="test1")
result = invoke("deckNames")
print(f"got list of decks: {result}")
