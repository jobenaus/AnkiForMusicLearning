import archiv.anki_connect as anki_connect
import init

import song_archive


def piano_piece(number_of_bars, difficulty=1):
    bar_names = init.make_bar_names(number_of_bars)
    if difficulty == 1:
        anki_connect.add_multiple_bars(1, 3, bar_names)
    elif difficulty == 2:
        anki_connect.add_multiple_bars(1, 1, bar_names, separate_hands=True)
        anki_connect.add_multiple_bars(2, 3, bar_names)
    elif difficulty == 3:
        anki_connect.add_single_bars(bar_names, separate_hands=True)
        anki_connect.add_multiple_bars(1, 3, bar_names)
    else:
        print("piano: difficulty not available")


def folk_song(url="", max_interval=3, bar_names=None):
    if bar_names == None:
        bar_names = song_archive.get_text(url)

    for j in range(1, max_interval + 1):
        for i in bar_names:
            try:

                front = str(j) + ": " + i + " (Text)"
                back = ""
                for k in range(1, j + 1):
                    back += bar_names[bar_names.index(i) + k] + " "
                anki_connect.add_note(front=front, back=back, separate_hands=False)
            except:
                print("error")

            try:

                front = str(j) + ": " + i + " (Gesang)"
                back = ""
                for k in range(1, j + 1):
                    back += bar_names[bar_names.index(i) + k] + " "
                anki_connect.add_note(front=front, back=back, separate_hands=False)
            except:
                print("error")
