from archiv.anki_connect import add_single_bars, add_multiple_bars
from init import make_bar_names
import archiv.anki_connect as anki_connect
import templates
import globals as glob

# deck information
glob.instrument = "Gesang"
glob.title = "La vendetta"
glob.composer = "Mozart"
glob.deck_suffix = ""

# settings
glob.test_mode = True
glob.override_deck = True

# init
anki_connect.init_deck()

# interface

bar_names = [
    "La vendetta, oh la vendetta,",
    "è un piacer serbato ai saggi,",
    "è un piacer serbato ai saggi. (2)",
    "L'obliar l'onte, e gl'oltraggi",
    "l'obliar l'onte, e gl' oltraggi (2)",
    "è bassezza, è ognor viltà,",
    "è bassezza, è ognor viltà, è ognor viltà.",
    "Coll' astuzia, coll' arguzia,",
    "col giudizio, col criterio,",
    "si protrebbe, si protrebbe,",
    "coll' astuzia, coll' arguzia, (2)",
    "col giudizio, col criterio, (2)",
    "si protrebbe, si protrebbe, (2)",
    "si protrebbe, si protrebbe... (3)",
    "il fatto è serio, ",
    "il fatto è serio, (2)",
    "il fatto è serio... (3)",
    "ma credete, si farà,",
    "ma credete, si farà. (2)",
    "Se tutto il codice dovessi volgere,",
    "se tutto l'indice dovessi leggere,",
    "con un equivoco, con un sinonimo",
    "qualche garbuglio si troverà,",
    "se tutto il codice dovessi volgere, (2)",
    "se tutto l'indice dovessi leggere, (2)",
    "con un equivoco, con un sinonimo (2)",
    "qualche garbuglio si troverà, (2)",
    "qualche garbuglio si troverà, si troverà.",
    "Tutta Siviglia conosce Bartolo,",
    "il birbo Figaro vostro sarà,",
    "tutta Siviglia conosce Bartolo, (2)",
    "il birbo Figaro vostro sarà, (2)",
    "il birbo Figaro vostro sarà, (3)",
    "il birbo Figaro vostro sarà, (4)",
    "vostro sarà, vostro sarà, vostro sarà.",
]

templates.folk_song(bar_names=bar_names)
