"""
Deck class is defined here.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Deck:
    """This class holds all the information of the deck that will be added to Anki."""

    def __init__(self, instrument: Optional[str], title: str, composer: Optional[str], suffix: Optional[str]):
        self.name = f"{title}"
        if instrument:
            self.name = f"{instrument}: " + f"{self.name}"
        if composer:
            self.name += f" - {composer}"
        if suffix:
            self.name += f" ({suffix})"

    name: str
    title: str

    instrument: Optional[str] = None
    composer: Optional[str] = None
    suffix: Optional[str] = None