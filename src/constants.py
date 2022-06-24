""" Lists all constants used in the application. """
# URLs
ANKI_CONNECT_URL = "http://localhost:8765"


# Strings used in the application.
CONNECTION_ERROR_MESSAGE = f"""
URLError: Could not reach: {ANKI_CONNECT_URL}. 
    Make sure that Anki is opened and AnkiConnect is installed.
"""

SETTINGS_FIXING_HINT = """
To restore the default settings, delete the settings.json file.
"""

# Defaults used in the application.
DEFAULT_SETTINGS = {"test_mode": True, "override_deck": False}
EXAMPLE_DECK_CREATION_DATA = {
    "deck_info": {
        "instrument": "Piano",
        "title": "Für Elise",
        "composer": "Beethoven",
        "suffix": "seperate hands",
    },
    "learning_style": {
        "memorize": False,
        "seperate_steps": ["RH", "LH"],
        "max_overlap": 3,
    },
    "items": [
        "Takt 1",
        "Takt 2",
        "Takt 3",
        "Takt 4",
        "Takt 5",
        "Takt 6",
        "Takt 7",
        "Takt 8",
        "Takt 9",
        "Takt 10",
    ],
}

# Filepaths used in the application.
SETTINGS_FILE = "src/settings.json"
DECK_CREATION_DATA_FILE = "src/deck_creation_data.json"
