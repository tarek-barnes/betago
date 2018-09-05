import random
from get_game_state import *

path = "../games/jgdb/"
MIN_MOVES = 30 #?

def get_list_filenames(path):
    new_path = path + "train.txt"
    f = open(new_path)
    data = f.read()
    filenames = data.split('\n')
    filenames = [k.replace("./", path) for k in filenames]
    return filenames

def get_training_states(path):
    training_testing = []
    training_filenames = get_list_filenames(path)
    training_filenames = training_filenames[3000:5000]
    for filename in training_filenames:
        try:
            total_moves = len(get_game_record(filename))
            if total_moves == 0:
                pass
            else:
                move_cap = random.choice(range(total_moves))
                if move_cap % 2 != 0:
                    move_cap -= 1
                try:
                    if not get_train_test_game_state(filename, move_cap):  # Testing
                        pass
                    else:
                        train, test = get_train_test_game_state(filename, move_cap)
                        training_testing.append((train,test))
                except ValueError:
                    pass
        except ValueError:
            pass
    return training_testing
