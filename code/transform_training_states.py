# get_training_states returns a list of tuples... [(x, y)], both as state arrays
# want: separate lists, y transformed to an integer

# game 23 is bad -- state k is the same as state k+1
# game 451 is also bad

import numpy as np
import pickle

def get_X_arrays(pickle_filename):
    with open(pickle_filename, "rb") as f:
        XY_arrays = pickle.load(f)
    X_arrays = [k[-2] for k in XY_arrays]
    return len(X_arrays)


def get_XY_delta(X_array, y_array):
    delta_array = y_array - X_array
    # find the tuple position of the 1
    row = [k for k in range(len(delta_array)) if 1 in delta_array[k]][0]
    col = int(np.where(delta_array[row] == 1)[0])
    x,y = (row+1, col+1)
    # translate that tuple into a 1D coordinate
    return ((x-1)*19 + y - 1)


def get_XY_arrays(pickle_filename):
    with open(pickle_filename, "rb") as f:
        generated_training_states = pickle.load(f)

    X_arrays, Y_arrays = [], []
    for entry in generated_training_states:
        _, _, _, X_array, Y_array = entry
        try:
            Y_arrays.append(get_XY_delta(X_array, Y_array))
            X_arrays.append(X_array)
        except:
            pass
    return list(zip(X_arrays, Y_arrays))


    # errors = 0
    # count = 0
    # for item in XY_arrays:
    #     X = item[-2]
    #     y = item[-1]
    #     delt = (y-X)
    #     try:
    #         Y_arrays.append(get_XY_delta(X,y))
    #         count += 1
    #     # except IndexError:
    #     except:
    #
    #         errors += 1
    #         print(f"count:{count}, {delt}")
    #         pass
    # return len(Y_arrays)

# print(get_X_arrays("jgdb_train_example.pickle"))
# print(get_Y_arrays("jgdb_train_example.pickle"))
