from anki_connect import add_single_bars, add_multiple_bars
from init import make_bar_names
import anki_connect
import globals as glob

# deck information
glob.instrument = "Violine"
glob.title = "Die Tapferkeit"
glob.composer = "Telemann"
glob.deck_suffix = ""

# settings
glob.test_mode = True
glob.override_deck = True

# init
anki_connect.init_deck()

# interface
bar_names = make_bar_names(53)

add_single_bars(bar_names, separate_hands=True)
add_multiple_bars(1,3, bar_names)


