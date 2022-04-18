import globals_v5 as glob


def make_bar_names(number_of_bars, first_bar = 1, repeats = {}, volta_type_a = {}, volta_type_b = {}):
    bar_names = []
    i = first_bar
    while i <= number_of_bars:
        if i in volta_type_a:
            for k in range(len(volta_type_a[i][1])):
                for j in range(1, volta_type_a[i][1][k] + 1):
                    bar_names.append(f"{i} {k + 1}.{j}")
                if k >= len(volta_type_a[i][1])-1:
                    break
                for j in range(volta_type_a[i][0], i):
                    bar_names.append(str(j))
        elif i in volta_type_b:
            for j in range(volta_type_b[i][1][0]):
                bar_names.append(str(i+j))
            for j in range(volta_type_b[i][0], i):
                bar_names.append(str(j))
            for j in range(volta_type_b[i][1][1]):
                bar_names.append(str(i + j + volta_type_b[i][1][0]))
            i = i + j + volta_type_b[i][1][0]
        else:
            bar_names.append(str(i))
        if i in repeats:

            for j in range(repeats[i],i + 1):
                bar_names.append(str(j))

        i += 1



    return bar_names

def make_deck_name():
    if glob.test_mode:
        deck_name = "test5: " + glob.instrument + ": " + glob.title + " - " + glob.composer + " " + glob.deck_suffix
    else:
        deck_name = glob.instrument + ": " + glob.title + " - " + glob.composer + " " + glob.deck_suffix
    return deck_name


