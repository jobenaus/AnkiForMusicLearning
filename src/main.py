"""
Python script for musicians that helps with adding notes to Anki.
"""

from typing import Any
from helpers import load_settings, load_deck_creation_data
from deck import Deck




def main() -> None:
    """Main function"""
    settings: dict[str, bool] = load_settings()
    print(f"settings: {settings}")
    deck_creation_data: dict[str, Any] = load_deck_creation_data()
    print(f"deck_creation_data: {deck_creation_data}")
    deck_info: dict[str, str] = deck_creation_data["deck_info"]
    test_deck: Deck = Deck(
        deck_info["instrument"],
        deck_info["title"],
        deck_info["composer"],
        deck_info["suffix"],
    )
    print(f"Deckname: {test_deck.name}")
    # TODO Load interface.txt
    # TODO Make List of items that shall be added to Anki
    # TODO Write to items.txt
    # TODO Open items.txt and ask user if he wants to change anything
    # TODO When user saves items.txt, ask user if he wants to add them to Anki
    # TODO Add items to Anki
    # TODO Give feedback what was added to Anki

    # Exit program
    exit(0)


if __name__ == "__main__":
    main()
