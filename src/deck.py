"""
Deck class is defined here.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Deck:
    """This class holds all the information of the deck that will be added to Anki."""

    title: str
    name: str = field(init=False)
    instrument: Optional[str] = None
    composer: Optional[str] = None
    suffix: Optional[str] = None

    def ___post_init___(self):
        """Add the Name of the deck."""
        self.name = compute_deck_name(
            self.instrument, self.title, self.composer, self.suffix
        )


def compute_deck_name(
    instrument: Optional[str],
    title: Optional[str],
    composer: Optional[str],
    suffix: Optional[str],
) -> str:
    """
    Compute the deck name.
    """
    name = f"{title}"
    if instrument:
        name = f"{instrument}: " + f"{name}"
    if composer:
        name += f" - {composer}"
    if suffix:
        name += f" ({suffix})"
    return name


# for testing purposes
if __name__ == "__main__":
    test_deck = Deck("Test Title")
    print(test_deck)
