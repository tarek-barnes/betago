import numpy as np
from get_game_record import *


def get_empty_board():
    return np.array([ [0]*19 ] * 19)


def is_on_board(position):
    x,y = position
    return ((x>0 and x<20) and (y>0 and y<20))


def is_legal_move(board, position):
    if is_on_board(position):
        x,y = position

        return board[x-1][y-1] == EMPTY


def color_to_num(color):
    if color == "B":
        return 1
    elif color == "W":
        return 2


def num_to_color(num):
    if num == 1:
        return "B"
    elif num == 2:
        return "W"


def pos_color(board, pos):
    x,y = pos
    return board[x-1][y-1]


def play_stone(board, position, color):
    # if is_on_board(position) and is_legal_move(board, position):
    if is_on_board(position):
        x,y = position
        board[x-1][y-1] = color_to_num(color)
        return board
    else:
        return "This move isn't legal"


def remove_stone(board, position):
    x,y = position
    if board[x-1][y-1] != 0:
        board[x-1][y-1] = 0
        return board
    else:
        return "There's no stone to remove"


def get_neighbors(position):
    x,y = position
    naive_neighbors = [(x-1, y), (x+1, y),
                       (x, y-1), (x, y+1)]
    return [k for k in naive_neighbors if is_on_board(k)]


def opposing(color):
    return 3 - color

# floodfill
def find_dead_stones(board, position):
    def has_liberties(pos, color):
        if pos_color(board, pos) == EMPTY:
            return True
        if pos_color(board, pos) == opposing(color):
            return False
        if pos in visited:
            return False

        visited.add(pos)
        neighbors = get_neighbors(pos)
        return any(has_liberties(n,color) for n in neighbors)

    dead_stones = []
    turn = pos_color(board, position)

    for neigh in get_neighbors(position):
        visited = set()
        if not has_liberties(neigh, opposing(turn)):
            dead_stones += list(visited)
    return dead_stones


def remove_dead_stones(board, position):
    dead_stones = find_dead_stones(board, position)
    for stone in dead_stones:
        remove_stone(board, stone)
    return board


def get_final_game_state(file_name):
    game_record = get_game_record(file_name)
    if game_record[0][0] != "B":
        return "W starts this game, error."

    board = get_empty_board()

    colors = [k[0] for k in game_record]
    positions = [k[1] for k in game_record]
    positions = [k.split("-") for k in positions]
    positions = [tuple(k) for k in positions]
    positions = [(int(a), int(b)) for a,b in positions]

    updated_record = list(zip(colors, positions))

    for record in updated_record:
        color, position = record
        play_stone(board, position, color)
        remove_dead_stones(board, position)

    return board





def example():
    board = get_empty_board()
    play_stone(board, (3,3), "B")
    play_stone(board, (3,2), "W")
    play_stone(board, (4,3), "W")
    play_stone(board, (2,3), "W")
    play_stone(board, (3,4), "W")
    return board

def example2():
    board = get_empty_board()
    play_stone(board, (3,3), "B")
    play_stone(board, (3,4), "B")
    play_stone(board, (3,2), "W")
    play_stone(board, (4,3), "W")
    play_stone(board, (2,3), "W")
    play_stone(board, (3,5), "W")
    play_stone(board, (2,4), "W")
    play_stone(board, (4,4), "W")
    return board

def example3():
    board = get_empty_board()
    play_stone(board, (5,4), "B")
    play_stone(board, (5,5), "B")
    play_stone(board, (6,5), "B")
    play_stone(board, (4,4), "W")
    play_stone(board, (4,5), "W")
    play_stone(board, (4,4), "W")
    play_stone(board, (5,6), "W")
    play_stone(board, (6,6), "W")
    play_stone(board, (7,5), "W")
    play_stone(board, (6,4), "W")
    play_stone(board, (5,3), "W")
    return board



EMPTY = 0
BLACK = 1
WHITE = 2
