from anki_connect import add_single_bars, add_multiple_bars
from init import make_bar_names
import anki_connect
import templates
import globals as glob

# deck information
glob.instrument = "Violine"
glob.title = "Allegro moderato"
glob.composer = "Gebauer"
glob.deck_suffix = "(Seperate Hands)"

# settings
glob.test_mode = True
glob.override_deck = True

# init
anki_connect.init_deck()

# interface
templates.folk_song(
    "https://www.lieder-archiv.de/wann_ich_des_morgens_frueh_aufsteh-notenblatt_300003.html"
)
