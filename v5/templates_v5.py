import anki_connect_v5
import init_v5
import globals_v5 as glob
from colorama import Fore
import song_archive_v5

def piano_piece(number_of_bars, difficulty = 1):
    bar_names = init_v5.make_bar_names(number_of_bars)
    if difficulty == 1:
        anki_connect_v5.add_multiple_bars(1, 3, bar_names)
    elif difficulty == 2:
        anki_connect_v5.add_multiple_bars(1, 1, bar_names, separate_hands=True)
        anki_connect_v5.add_multiple_bars(2, 3, bar_names)
    elif difficulty == 3:
        anki_connect_v5.add_single_bars(bar_names, separate_hands=True)
        anki_connect_v5.add_multiple_bars(1, 3, bar_names)
    else:
        print(Fore.RED + "piano: difficulty not available")

def folk_song(url, max_interval = 3):
    bar_names =song_archive_v5.get_text(url)

    for j in range(1, max_interval + 1):
        for i in bar_names:
            try:

                front = str(j) + ": " + i + " (Text)"
                back = ""
                for k in range(1, j + 1):
                    back += bar_names[bar_names.index(i) + k] + " "
                anki_connect_v5.add_note(front=front, back=back, separate_hands=False)
            except:
                print("error")

    for j in range(1, max_interval + 1):
        for i in bar_names:
            try:

                front = str(j) + ": " + i + " (Gesang)"
                back = ""
                for k in range(1, j + 1):
                    back += bar_names[bar_names.index(i) + k] + " "
                anki_connect_v5.add_note(front=front, back=back, separate_hands=False)
            except:
                print("error")