import anki_connect
import init
from classes import Deck


# deck information
instrument = "Violine"
piece_title = "Cappricio"
composer = "Grazyna Bracewicz"
deck_suffix = "suffix"

# settings
test_mode = True
override_deck = True

# create deck
deck = Deck(piece_title, composer, instrument, deck_suffix)

# set deck settings
deck.test_mode = test_mode


deck.override_deck = override_deck


# interface
if __name__ == "__main__":
    # create deck
    anki_connect.init_deck(deck.name)

    # make item_list
    bar_names = init.make_bar_names(10, volta_type_a={6: [2, [2, 4]]})

    # create notes
    # anki_connect.add_single_bars(deck.name, bar_names)
    anki_connect.add_multiple_bars(deck.name, 1, 3, bar_names)
