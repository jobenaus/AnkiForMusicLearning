"""
Python script for musicians that helps with adding notes to Anki.
"""
from helpers import load_settings, load_deck_creation_data


def main():
    """Main function"""
    settings = load_settings()
    print(f"settings: {settings}")
    deck_creation_data = load_deck_creation_data()
    print(f"deck_creation_data: {deck_creation_data}")
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
