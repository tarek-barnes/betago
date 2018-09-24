from get_game_state import *
import numpy as np
import pickle
import random

PATH = "../games/jgdb/"


def get_file_names(PATH):
    new_path = PATH + "test.txt"
    f = open(new_path)
    data = f.read()
    file_names = data.split('\n')
    file_names = [k.replace("./", PATH) for k in file_names]
    return file_names

def are_the_same(array_A, array_B):
    return (array_A == array_B).all()

def are_too_close(total_moves, current_move, threshold):
    return (total_moves - current_move) < threshold

def get_random_state(file_name):
    try:
        total_moves = len(get_game_record(file_name))
        if total_moves <= 5:
            return False
    except:
        return False

    threshold = 4
    while True:
        current_move = random.choice(range(total_moves))
        if current_move % 2 != 0:  # ensure B
            current_move -= 1
        if are_too_close(total_moves, current_move, threshold):
            current_move -= threshold
        try:
            train, test = get_train_test_game_state(file_name, current_move)
            if not are_the_same(train, test):
                return (total_moves, current_move, file_name, train, test)
        except:
            return False


def generate_random_states(PATH):
    file_names = get_file_names(PATH)
    file_names = file_names[:100]  # testing
    training_states = list(map(get_random_state, file_names))
    training_states = [k for k in training_states if k]
    return training_states


def get_board_rotations(train_state, test_state):
    rotations = []
    for k in range(3):
        train_state = np.rot90(train_state)
        test_state = np.rot90(test_state)
        rotations.append((train_state, test_state))
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
            train, test = get_train_test_game_state(file_name, current_move)
            if not are_the_same(train, test):
                many_states.append((total_moves,
                                    current_move,
                                    file_name,
                                    train,
                                    test))
                for rotation in get_board_rotations(train, test):
                    train_rotation, test_rotation = rotation
                    many_states.append((total_moves,
                                        current_move,
                                        file_name,
                                        train_rotation,
                                        test_rotation))
            current_move += step
        except:
            return False
    return many_states


def generate_many_game_states(PATH):
    file_names = get_file_names(PATH)
    # file_names = file_names[:10]  # testing
    many_game_states = list(map(get_game_states, file_names))
    many_game_states = [k for k in many_game_states if k]
    many_game_states = [k for row in many_game_states for k in row]
    return many_game_states


def flatten_Y_array(X_array, Y_array):
    delta = Y_array - X_array
    Y_row = [k for k in range(len(delta)) if 1 in delta[k]][0]
    Y_col = int(np.where(delta[Y_row] == 1)[0])
    x, y = (Y_row+1, Y_col+1)
    return ((x - 1) * 19 + y)


def generate_training_states(lst_of_states):
    state_info, X_arrays, Y_arrays = [], [], []
    for entry in lst_of_states:
        total_moves, current_move, file_name, X_array, Y_array = entry
        try:
            Y_arrays.append(flatten_Y_array(X_array, Y_array))
            X_arrays.append(X_array)
            state_info.append((total_moves, current_move, file_name))
        except:
            pass
    return list(zip(state_info, X_arrays, Y_arrays))


def get_policy_states():
    game_states = generate_many_game_states(PATH)
    training_states = generate_training_states(game_states)
    with open("policy_train_states.pickle", "wb") as f:
        pickle.dump(training_states, f)
