# How to connect to anki

## Minimum Requirements:
- create a deck from json data
  - check if deck already exists
  - sanitise json input
  - make api request to create deck
  
### Flashcard types
- Basic, (Cloze)

### API requests


CREATE DECK

request
{
    "action": "createDeck",
    "version": 6,
    "params": {
        "deck": "Japanese::Tokyo"
    }
}

result
{
    "result": 1519323742721,
    "error": null
}

-> handle error if deck already exists


ADD NOTE

request
{
    "action": "addNote",
    "version": 6,
    "params": {
        "note": {
            "deckName": "Default",
            "modelName": "Basic",
            "fields": {
                "Front": "front content",
                "Back": "back content"
            },
            "options": {
                "allowDuplicate": false,
                "duplicateScope": "deck",
                "duplicateScopeOptions": {
                    "deckName": "Default",
                    "checkChildren": false,
                    "checkAllModels": false
                }
            },
            "tags": [
                "yomichan"
            ],
            "audio": [{
                "url": "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji=猫&kana=ねこ",
                "filename": "yomichan_ねこ_猫.mp3",
                "skipHash": "7e2c2f954ef6051373ba916f000168dc",
                "fields": [
                    "Front"
                ]
            }],
            "video": [{
                "url": "https://cdn.videvo.net/videvo_files/video/free/2015-06/small_watermarked/Contador_Glam_preview.mp4",
                "filename": "countdown.mp4",
                "skipHash": "4117e8aab0d37534d9c8eac362388bbe",
                "fields": [
                    "Back"
                ]
            }],
            "picture": [{
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                "filename": "black_cat.jpg",
                "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                "fields": [
                    "Back"
                ]
            }]
        }
    }
}

result
{
    "result": 1496198395707,
    "error": null
}

-> handle error if note already exists

### Model
class Deck {
    name: string
    notes: list(Note)
}

class Note {
    content: NoteContent
}

class NoteContent(ABC):
    abc

class BasicContent(NoteContent):
    front: NoteField
    back: NoteField

class ClozeContent(NoteContent):
    front: NoteField

class NoteField:
    text: string

class Media:
    TODO later


Composition:
use ABCs to seperate responibilities
inherit from abcs to reduce duplication
compose everything in the super_class