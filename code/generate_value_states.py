from get_game_record import *
from get_game_state import *
import numpy as np

PATH = "../games/jgdb/"

def get_file_names(PATH):
    new_path = PATH + "train.txt"
    f = open(new_path)
    data = f.read()
    file_names = data.split('\n')
    file_names = [k.replace("./", PATH) for k in file_names]
    return file_names


def get_value_state(file_name, move_cap):
    board = get_empty_board()
    winner = get_game_winner(file_name)

    updated_record = get_updated_game_record(file_name)
    if not updated_record:  # Testing
        return False

    # if move_cap is even, last move is W (0-indexed)
    train_record = updated_record[:move_cap]
    for record in train_record:
        color, position = record
        play_stone(board, position, color)
        remove_dead_stones(board, position)

    return (board, winner)


def get_board_rotations(board):
    rotations = []
    for k in range(3):
        board = np.rot90(board)
        rotations.append(board)
    return rotations


def get_game_states(file_name):
    try:
        total_moves = len(get_game_record(file_name))
        if total_moves <= 5:
            print("one")
            return False
    except:
        print("two")
        return False

    many_states = []
    step = 6
    starting_move = 2
    current_move = starting_move
    while total_moves > (current_move + 4):
        try:
            board, winner = get_value_state(file_name, current_move)
            print(f"board: {board}\n winner: {winner}")
            many_states.append((total_moves,
                                current_move,
                                file_name,
                                board,
                                winner))
            k = len(many_states)
            print(f"len of many_states: {k}")
            for rotation in get_board_rotations(board):
                many_states.append((total_moves,
                                    current_move,
                                    file_name,
                                    rotation,
                                    winner))
            j = len(many_states)
            print(f"len of many_states: {j}")
            current_move += step
        except:
            print("three")
            return False
    return many_states


def generate_many_game_states(PATH):
    file_names = get_file_names(PATH)
    file_names = file_names[:10]  # testing
    many_game_states = list(map(get_game_states, file_names))
    many_game_states = [k for k in many_game_states if k]
    many_game_states = [k for row in many_game_states for k in row]
    return many_game_states


def generate_training_states(lst_of_states):
    state_info, boards, winners = [], [], []
    for entry in lst_of_states:
        total_moves, current_move, file_name, board, winner = entry
        try:
            winners.append(winner)
            boards.append(board)
            state_info.append((total_moves, current_move, file_name))
        except:
            pass
    return list(zip(state_info, boards, winners))


def get_value_states():
    game_states = generate_many_game_states(PATH)
    training_states = generate_training_states(game_states)
    with open("value_train_states.pickle", "wb") as f:
        pickle.dump(training_states, f)
