"""
Deck class is defined here.
"""
from dataclasses import dataclass


@dataclass
class Deck:
    """This class holds all the information of the deck that will be added to Anki."""

    def __init__(self, instrument, title, composer, suffix):
        self.name = f"{title}"
        if instrument:
            self.name = f"{instrument}: " + f"{self.name}"
        if composer:
            self.name += f" - {composer}"
        if suffix:
            self.name += f" ({suffix})"

    name: str
    title: str

    instrument: str = None
    composer: str = None
    suffix: str = None
