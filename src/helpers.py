"""Contains helper functions for the main program."""

import json
from constants import SETTINGS_FILE, SETTINGS_FIXING_HINT, DEFAULT_SETTINGS


def load_settings():
    """Loads settings from settings.json."""
    try:
        with open(SETTINGS_FILE, encoding="utf8") as settings_file:
            settings = json.load(settings_file)
    except FileNotFoundError:
        print("settings.json not found.")
        create_default_settings()
        return DEFAULT_SETTINGS

    except json.decoder.JSONDecodeError as err:
        print("settings.json is not valid json.")
        ask_to_fix_settings(err)

    # settings.json is empty
    if not settings:
        print("settings.json is empty.")
        create_default_settings()
        return DEFAULT_SETTINGS

    # settings.json misses some keys
    if not all(key in settings for key in DEFAULT_SETTINGS):
        print("settings.json is missing keys.")
        ask_to_fix_settings(KeyError)

    # settings.json has invalid types
    if not all(
        isinstance(settings[key], type(DEFAULT_SETTINGS[key]))
        for key in DEFAULT_SETTINGS
    ):
        print("settings.json has invalid types.")
        ask_to_fix_settings(TypeError)

    # check if settings.json has keys that are not in default_settings
    if any(key not in DEFAULT_SETTINGS for key in settings):
        print("Some keys in settings.json are not in default_settings.")
        return DEFAULT_SETTINGS

    return settings


def create_default_settings():
    """Creates a default settings.json file."""
    with open(SETTINGS_FILE, "w", encoding="utf8") as settings_file:
        json.dump(DEFAULT_SETTINGS, settings_file)

    print("Created default settings.json file.")


def ask_to_fix_settings(err):
    """Asks the user to fix the settings.json file."""
    print(SETTINGS_FIXING_HINT)
    raise SystemExit(err) from err
