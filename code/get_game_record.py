# Convert SGF (Go Game) -> list of moves as tuples: e.g. ("W", 4-18)
# Top left corner is (1-1), bottom right is (19-19)

import csv

EMPTY = 0
BLACK = 1
WHITE = 2

def get_raw_game(file_name):
    f = open(file_name, "rb")
    raw_game = f.read()
    raw_game = str(raw_game)
    return raw_game


def get_game_winner(file_name):
    raw_game = get_raw_game(file_name)
    if "RE" not in raw_game:
        return False
    result_start = raw_game.index("RE")
    game = raw_game[result_start:]
    result_end = game.index("]")
    game_result = game[:(result_end + 1)]
    if "B" in game_result:
        return BLACK
    elif "W" in game_result:
        return WHITE
    else:
        return False


def get_game_record(file_name):
    def make_index(raw_coordinate):
        coord_mapper = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1,27)))
        i = str(coord_mapper[raw_coordinate[-1]])
        j = str(coord_mapper[raw_coordinate[0]])
        coord = i + "-" + j
        return coord

    raw_game = get_raw_game(file_name)
    game = raw_game.split(";")[2:]
    game = [k.replace("\\n", "") for k in game]
    game = [k.replace(")\n", "") for k in game]
    game = [k.replace(")'", "") for k in game]
    game = [k.replace("[", " [") for k in game]
    game = [k.replace("[", "").replace("]", "") for k in game]
    game = [tuple(k.split(" ")) for k in game]

    parsed_game = []
    for move in game:
        color, position = move
        parsed_game.append((color, make_index(position)))

    return parsed_game
