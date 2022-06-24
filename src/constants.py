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

# Filepaths used in the application.
SETTINGS_FILE = "src/settings.json"
