import keras
import pickle
import numpy as np
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.layers import (
    Dense,
    Input,
    Flatten,
    Conv2D,
    MaxPooling2D,
    Dropout)


# CHECKPOINT_PATH = "/Users/tarekbarnes/github/project_kojak/data/checkpoint.hdf5"
# DATA_PATH = "/Users/tarekbarnes/github/project_kojak/data/"

CHECKPOINT_PATH = "/data2/data/checkpoint.hdf5"
DATA_PATH = "/data2/data/"

def train_model(model, training_states, validation_states):
    # # Create an input (object) - size, shape
    # model_input = Input(shape=(19, 19, 1))
    # # Take the output of that input and pass it through some # of layers
    # x = Conv2D(filters=128, kernel_size=3, padding="same", activation="relu")(model_input)
    # x = MaxPooling2D()(x)
    # x = Conv2D(filters=192, kernel_size=3, padding="same", activation="relu")(x)  # kernel_size is window size, check alphago window_size
    # x = MaxPooling2D()(x)
    # x = Conv2D(filters=256, kernel_size=3, padding="same", activation="relu")(x)
    # x = MaxPooling2D()(x)
    #
    # x = Flatten()(x)
    # x = Dense(128, activation="relu")(x)   # change to sigmoid?
    # x = Dropout(0.4)(x)
    # model_output = Dense(361, activation="softmax")(x)
    #
    # # Use input and output to define model
    # model = Model(input=model_input, output=model_output)

    try:
        model.load_weights(CHECKPOINT_PATH)
    except:
        pass

    # Compile model w/ optimizer and loss function and callbacks
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])

    check_pointer = ModelCheckpoint(filepath=CHECKPOINT_PATH,
                                    save_best_only=True,
                                    mode="auto",
                                    monitor="val_acc") #I can also change this to val_loss

    X_train = [k[-2] for k in training_states]
    X_train = [k.reshape(19,19,1) for k in X_train]
    y_train = [k[-1] - 1 for k in training_states]

    X_val = [k[-2] for k in validation_states]
    X_val = [k.reshape(19, 19, 1) for k in X_val]
    y_val = [k[-1] - 1 for k in validation_states]

    # print(X_train[0].shape)
    model.fit(np.array(X_train).reshape(-1,19,19,1),
              np.array(y_train).reshape(-1),
              batch_size=128,
              epochs=13,
              validation_data=(np.array(X_val).reshape(-1,19,19,1), np.array(y_val).reshape(-1)),
              callbacks=[check_pointer])

    # use model.predict
    print(model.summary())



# Create an input (object) - size, shape
model_input = Input(shape=(19, 19, 1))
# Take the output of that input and pass it through some # of layers
x = Conv2D(filters=128, kernel_size=3, padding="same", activation="relu")(model_input)
x = MaxPooling2D()(x)
x = Conv2D(filters=192, kernel_size=3, padding="same", activation="relu")(x)  # kernel_size is window size, check alphago window_size
x = MaxPooling2D()(x)
x = Conv2D(filters=256, kernel_size=3, padding="same", activation="relu")(x)
x = MaxPooling2D()(x)

x = Flatten()(x)
x = Dense(128, activation="relu")(x)   # change to sigmoid?
x = Dropout(0.4)(x)
model_output = Dense(361, activation="softmax")(x)

# Use input and output to define model
model = Model(input=model_input, output=model_output)


train_shell = "policy_training/policy_train_states{}.pickle"
val_shell = "policy_val/policy_val_states{}.pickle"

for k in range(51):
    n = str(k)
    train_filename = train_shell.format(n)
    train_location = DATA_PATH + train_filename
    print(f"Using training file: {train_location}")
    val_filename = val_shell.format(n)
    val_location = DATA_PATH + val_filename
    print(f"Using validation file: {val_location}")

    # Get train/val data
    print("Loading training data...")
    with open(train_location, "rb") as f:
        training_states = pickle.load(f)
    print("Training data loaded")
    print("Loading validation data...")
    with open(val_location, "rb") as f:
        validation_states = pickle.load(f)
    print("Validation data loaded")    

    print("----------------------------------------")
    print(f"\nBEGIN: TRAINING FILE: {n}/50:\n")
    print("----------------------------------------")

    train_model(model, training_states, validation_states)

    print("----------------------------------------")
    print(f"\nCOMPLETED: TRAINING FILE: {n}/50:\n")
    print("----------------------------------------")
    del training_states
    del validation_states




# # Get train/val data
# with open("jgdb_train_states.pickle", "rb") as f:
#     training_states = pickle.load(f)
# with open("jgdb_val_states.pickle", "rb") as f:
#     val_states = pickle.load(f)
