import json
import urllib.request
from tqdm import tqdm
import init_v5
import globals_v5 as glob




def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    request_json = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', request_json)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


def create_deck(name):
    invoke("createDeck", deck=name)
    print("new deck created: {}".format(name))


def delete_deck(name, cards_too=False):
    invoke("deleteDecks", decks=[name], cardsToo=cards_too)
    print("deck deleted: {}".format(name))

def init_deck():
    name = init_v5.make_deck_name()
    if glob.override_deck:
        delete_deck(name=name, cards_too=True)
    create_deck(name)


def add_note(front="", back="", modelName="Basic", allow_duplicate=False, duplicate_scope="deck",
             separate_hands=False):
    deckName = init_v5.make_deck_name()
    front_suffix = ""
    if separate_hands:
        for i in range(3):
            if i == 0:
                front_suffix = "(RH)"
            if i == 1:
                front_suffix = "(LH)"
            if i == 2:
                front_suffix = ""

            invoke("addNote", note={
                "deckName": deckName,
                "modelName": modelName,
                "fields": {
                    "Front": front + " " + front_suffix,
                    "Back": back
                },
                "options": {
                    "allowDuplicate": allow_duplicate,
                    "duplicateScope": duplicate_scope
                }
            })

    else:
        invoke("addNote", note={
            "deckName": deckName,
            "modelName": modelName,
            "fields": {
                "Front": front + " "+ front_suffix,
                "Back": back
            },
            "options": {
                "allowDuplicate": allow_duplicate,
                "duplicateScope": duplicate_scope
            }
        })


def add_single_bars(bar_names, separate_hands = False):
    for i in tqdm(bar_names):
        try:
            add_note(front="Takt " + i, separate_hands=separate_hands)
        except:
            print(f"error single bar: {i}")
            #for j in i:
            #    try:
            #        add_note("Takt " + j, separate_hands=separate_hands)
            #    except:
            #        for k in j:
             #           try:
             #               add_note("Takt " + k, separate_hands=separate_hands)
                #        except:
             #               print(f"{k} is not a string")

def add_multiple_bars(min_interval, max_interval, bar_names, separate_hands=False):

    for k in tqdm(range(min_interval, max_interval+1)):
        for i in tqdm(range(len(bar_names))):

            if i - k >= 0:


                try:
                    add_note(front="Takt " + bar_names[i - k] + " - " + bar_names[i], separate_hands=separate_hands)

                except:
                    print(f"duplicate with i: {i}, k: {k}")


