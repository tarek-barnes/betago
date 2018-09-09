import keras
import pickle
from keras.models import Model
from keras.callbacks import ModelCheckPoint
from keras.layers import (
    Dense,
    Input,
    Flatten,
    Conv2D,
    MaxPooling2D,
    Dropout)

# call np.array(X) for X = [array1, array2, ...] (might not matter)
# after i do this, call X[:, :, :, np.newaxis]

PATH = "/Users/tarekbarnes/github/project_kojak/data/checkpoint.hdf5"

# Create an input (object) - size, shape
model_input = Input(shape=(19, 19, 1))

# Take the output of that input and pass it through some # of layers
x = Conv2D(filters=8, kernel_size=3, padding="same", activation="relu")(model_input)
x = MaxPooling2D()(x)
x = Conv2D(filters=16, kernel_size=3, padding="same", activation="relu")(x)  # kernel_size is window size, check alphago window_size
x = MaxPooling2D()(x)
x = Conv2D(filters=32, kernel_size=3, padding="same", activation="relu")(x)
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

check_pointer = ModelCheckPoint(filepath=PATH,
                                save_best_only=True,
                                monitor="accuracy") #I can also change this to val_loss


# Get train/val data
with open("jgdb_train_states.pickle", "rb") as f:
    training_states = pickle.load(f)
with open("jgdb_val_states.pickle", "rb") as f:
    val_states = pickle.load(f)

X_train = [k[1] for k in training_states]
y_train = [k[2] for k in training_states]
X_val = [k[1] for k in val_states]
y_val = [k[1] for k in val_states]



model.fit(X_train,
          y_train,
          batch_size=128,
          epochs=1,              # Increase this later, ~10? Also check batch_size
          validation_data=(X_val, y_val),
          callbacks=[check_pointer])

model.load_weights(PATH)

# consider saving model once I'm done

print(model.summary())
