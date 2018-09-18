import pickle
import random

def partition_validation_data(pickled_file_name):
    def partition(lst, n):
        division = len(lst) / float(n)
        return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]

    with open(pickled_file_name, "rb") as f:
        validation_states = pickle.load(f)

    random.shuffle(validation_states)
    parts = partition(validation_states, 51)
    name_nomenclature = "policy_val_states{}.pickle"

    for part in parts:
        n = str(parts.index(part))
        print(f"working on part {n}")
        with open(name_nomenclature.format(n), "wb") as f:
            pickle.dump(part, f)


def partition_training_data(pickled_file_name):
    def partition(lst, n):
        division = len(lst) / float(n)
        return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]

    with open(pickled_file_name, "rb") as f:
        training_states = pickle.load(f)

    random.shuffle(training_states)
    parts = partition(training_states, 51)
    name_nomenclature = "policy_train_states{}.pickle"

    for part in parts:
        n = str(parts.index(part))
        print(f"working on part {n}")
        with open(name_nomenclature.format(n), "wb") as f:
            pickle.dump(part, f)
