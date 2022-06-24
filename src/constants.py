""" Lists all constants used in the application. """
ANKI_CONNECT_URL = "http://localhost:8765"


# Strings used in the application.
CONNECTION_ERROR_MESSAGE = f"""
URLError: Could not reach: {ANKI_CONNECT_URL}. 
    Make sure that Anki is opened and AnkiConnect is installed.
"""

SETTINGS_FIXING_HINT = """
To restore the default settings, delete the settings.json file.
"""

# Default files used in the application.
SETTINGS_FILE = "src/settings.json"
