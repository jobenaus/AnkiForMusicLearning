"""Contains helper functions for the main program."""
import json


def load_settings():
    """Loads settings from settings.json."""
    with open("settings.json", encoding="utf8") as settings_file:
        settings = json.load(settings_file)
    return settings
