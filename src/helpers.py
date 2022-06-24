"""Contains helper functions for the main program."""

import json
from constants import SETTINGS_FILE, SETTINGS_FIXING_HINT

default_settings = {"test_mode": True, "override_deck": False, "name": "Default Deck"}


def load_settings():
    """Loads settings from settings.json."""
    try:
        with open(SETTINGS_FILE, encoding="utf8") as settings_file:
            settings = json.load(settings_file)
    except FileNotFoundError:
        print("settings.json not found.")
        create_default_settings()
        return default_settings

    except json.decoder.JSONDecodeError as err:
        print("settings.json is not valid json.")
        ask_to_fix_settings(err)

    if not settings:
        print("settings.json is empty.")
        create_default_settings()
        return default_settings

    if not isinstance(settings, dict):
        print("settings.json is not a dictionary.")
        ask_to_fix_settings(TypeError)

    if not all(key in settings for key in default_settings):
        print("settings.json is missing keys.")
        ask_to_fix_settings(KeyError)

    if not all(
        isinstance(settings[key], type(default_settings[key]))
        for key in default_settings
    ):
        print("settings.json has invalid types.")
        ask_to_fix_settings(TypeError)

    # check if settings.json has keys that are not in default_settings
    if any(key not in default_settings for key in settings):
        print("Some keys in settings.json are not in default_settings.")
        return default_settings

    return settings


def create_default_settings():
    """Creates a default settings.json file."""
    with open(SETTINGS_FILE, "w", encoding="utf8") as settings_file:
        json.dump(default_settings, settings_file)

    print("Created default settings.json file.")


def ask_to_fix_settings(err):
    """Asks the user to fix the settings.json file."""
    print(SETTINGS_FIXING_HINT)
    raise SystemExit(err) from err
