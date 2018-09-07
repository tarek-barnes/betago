# For jgdp dataset, generate tuples of input/output game states for position k (randomly chosen) for policy network

import pickle
import random
import numpy as np
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


def are_the_same(array_A, array_B):
    return (array_A == array_B).all()


def generate_training_states(path):
    def generate_random_state(filename):
        try:
            number_moves = len(get_game_record(filename))
            if number_moves == 0:
                return None
        except:
            return None

        attempts = 0
        while True:
            move_cap = random.choice(range(number_moves))
            end_padding = 6
            if move_cap % 2 != 0:
                move_cap -= 1
            if (number_moves - move_cap) < end_padding:
                move_cap -= end_padding

            try:
                attempts += 1
                train, test = get_train_test_game_state(filename, move_cap)
                if not are_the_same(train, test):
                    return (number_moves, move_cap, filename, train, test)
                if counts > 10:
                    return None
            except:
                return None


        # pass

    # count = 0
    # training_testing = []
    training_filenames = get_list_filenames(path)
    training_filenames = training_filenames[:50000]
    training_testing = list(map(generate_random_state, training_filenames))
    training_testing = [k for k in training_testing if k]
    # for filename in training_filenames:
    #     try:
    #         total_moves = len(get_game_record(filename))
    #         if total_moves == 0:  # Testing
    #             pass
    #         else:
    #             move_cap = random.choice(range(total_moves))
    #             while True:
    #                 if (total_moves - move_cap) < 6:  # Testing
    #                     move_cap = random.choice(range(total_moves))
    #                 break
    #             if move_cap % 2 != 0:
    #                 move_cap -= 1
    #             try:
    #                 if not get_train_test_game_state(filename, move_cap):  # Testing
    #                     pass
    #                 else:
    #                     train, test = get_train_test_game_state(filename, move_cap)
    #                     count += 1
    #                     print(f"OK-{count}, filename-{filename}, movecap-{move_cap}")
    #                     training_testing.append((train,test))
    #             except ValueError:
    #                 pass
    #     except (ValueError, KeyError):
    #         pass
    return training_testing
#
training_states = generate_training_states(path)
with open("jgdb_train_example.pickle", "wb") as f:
    pickle.dump(training_states, f)
