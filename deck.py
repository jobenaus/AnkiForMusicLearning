import anki_connect

from settings import Settings

class Deck(Settings):
    instrument: str
    piece_title: str
    composer: str
    title_suffix: str

    def __init__(self, piece_title="unknown title", composer="unknown composer", instrument=None, title_suffix=None):
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

        if Settings.test_mode:
            name = f"[TEST] {name}"

        return name

    def create_in_anki(self):
        anki_connect.invoke("createDeck", deck=self.name)

        return f"Deck '{self.name}' was created in Anki."
