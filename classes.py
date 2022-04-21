class DeckSettings:
    test_mode = True
    override_deck = True

class Deck(DeckSettings):
    def __init__(self, piece_title = "unknown title", composer = "unknown composer", instrument= None, title_suffix=None):
        self.instrument = instrument
        self.piece_title = piece_title
        self.composer = composer
        self.title_suffix = title_suffix

    @property
    def name(self):
        name = f"{self.piece_title} - {self.composer}"
        if self.instrument:
            name = f"{self.instrument}: {name}"

        if self.title_suffix:
            name += f" ({self.title_suffix})"


        if self.test_mode:
            name = f"[TEST] {name}"


        return name


