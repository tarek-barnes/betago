import csv

def get_game_record(file_name):
    def get_raw_game():
        f = open(file_name, "rb")
        raw_game = f.read()
        raw_game = str(raw_game)
        return raw_game

    def make_index(raw_coordinate):
        coord_mapper = dict(zip("abcdefghijklmnopqrstuvwxyz", range(1,27)))
        i = str(coord_mapper[raw_coordinate[-1]])
        j = str(coord_mapper[raw_coordinate[0]])
        coord = i + "-" + j
        return coord

    raw_game = get_raw_game()
    game = raw_game.split(";")[2:]
    game = [k.replace("\\n", "") for k in game]
    game = [k.replace(")'", "") for k in game]
    game = [k.replace("[", " [") for k in game]
    game = [k.replace("[", "").replace("]", "") for k in game]
    game = [tuple(k.split(" ")) for k in game]

    parsed_game = []
    for move in game:
        color, position = move
        parsed_game.append((color, make_index(position)))

    return parsed_game
