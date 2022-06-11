from anki_connect import add_single_bars, add_multiple_bars
from init import make_bar_names
import anki_connect
import templates
import globals as glob

# deck information
glob.instrument = "Gesang"
glob.title = "Flow my tears"
glob.composer = "Dowland"
glob.deck_suffix = ""

# settings
glob.test_mode = True
glob.override_deck = True

# init
anki_connect.init_deck()

# interface

bar_names = [
    "Flow my tears fall from your springs,",
    "Exil'd forever let me mourn:",
    "Where night's black bird her sad infamy sings,",
    "There let me live forlorn.",
    "Down vain lights shine you no more,",
    "No nights are dark enough for those",
    "That in despair their last fortunes deplore,",
    "Light doth but shame disclose.",
    "Never may my woes be relieved,",
    "Since pity is fled, ",
    "And tears, and sighs, and groans",
    "my weary days, my weary days",
    "Of all joys have deprived.",
    "From the highest spire of contentment,",
    "My fortune is thrown,",
    "And fear, and grief, and pain",
    "for my deserts, for my deserts,",
    "Are my hopes since hope is gone.",
    "Hark you shadows that in darkness dwell,",
    "Learn to contemn light,",
    "Happy, happy they that in hell",
    "Feel not the world's despite.",
    "Hark you shadows that in darkness dwell, (2)",
    "Learn to contemn light, (2)",
    "Happy, happy they that in hell (2)",
    "Feel not the world's despite. (2)",
]

templates.folk_song(bar_names=bar_names)
