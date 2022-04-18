from anki_connect_v5 import add_single_bars, add_multiple_bars
from init_v5 import make_bar_names, make_deck_name
import anki_connect_v5
import templates_v5 as temp
import globals_v5 as glob

# deck information
glob.instrument = "Violine"
glob.title = "Cappricio"
glob.composer = ""
glob.deck_suffix = "Seperate Hands"

# settings
glob.test_mode = False
glob.override_deck = True

# init
anki_connect_v5.init_deck()

# interface
bar_names = make_bar_names(53)

add_single_bars(bar_names, separate_hands=True)
add_multiple_bars(1,3, bar_names)


