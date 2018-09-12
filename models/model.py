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

PATH = "/Users/tarekbarnes/github/project_kojak/data/checkpoint.hdf5"

# Create an input (object) - size, shape
model_input = Input(shape=(19, 19, 1))

# Take the output of that input and pass it through some # of layers
x = Conv2D(filters=128, kernel_size=8, padding="same", activation="relu")(model_input)
x = MaxPooling2D()(x)
x = Conv2D(filters=128, kernel_size=8, padding="same", activation="relu")(x)  # kernel_size is window size, check alphago window_size
x = MaxPooling2D()(x)
x = Conv2D(filters=128, kernel_size=8, padding="same", activation="relu")(x)
x = MaxPooling2D()(x)

x = Flatten()(x)
x = Dense(128, activation="relu")(x)   # change to sigmoid?
model_output = Dense(361, activation="softmax")(x)

# Use input and output to define model
model = Model(input=model_input, output=model_output)

# Compile model w/ optimizer and loss function and callbacks
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

check_pointer = ModelCheckpoint(filepath=PATH,
                                save_best_only=True,
                                mode="auto",
                                monitor="val_acc") #I can also change this to val_loss


# Get train/val data
with open("jgdb_train_states.pickle", "rb") as f:
    training_states = pickle.load(f)
with open("jgdb_val_states.pickle", "rb") as f:
    val_states = pickle.load(f)

X_train = [k[-2] for k in training_states]
X_train = [k.reshape(19,19,1) for k in X_train]
y_train = [k[-1] - 1 for k in training_states]

X_val = [k[-2] for k in val_states]
X_Val = [k.reshape(19, 19, 1) for k in X_val]
y_val = [k[-1] - 1 for k in val_states]

# print(X_train[0].shape)
model.fit(np.array(X_train).reshape(-1,19,19,1),
          np.array(y_train).reshape(-1),
          batch_size=128,
          epochs=1,
          validation_data=(np.array(X_val).reshape(-1,19,19,1), np.array(y_val).reshape(-1)),
          callbacks=[check_pointer])

# model.load_weights(PATH)

# use model.predict



print(model.summary())
