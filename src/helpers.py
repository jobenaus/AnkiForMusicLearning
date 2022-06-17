"""Contains helper functions for the main program."""

import json


def load_settings():
    """Loads settings from settings.json."""
    try:
        with open("settings.json", encoding="utf8") as settings_file:
            settings = json.load(settings_file)
    except FileNotFoundError as exc:
        raise FileNotFoundError("settings.json not found") from exc

        # TODO create default settings.json file if no settings.json file is present

    return settings
