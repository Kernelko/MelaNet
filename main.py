#Awesome neural network
# to set theano as backend run in terminal:
#set "KERAS_BACKEND=theano"

import theano
import keras
import numpy as np
np.random.seed(123)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist

from matplotlib import pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 1, 28,28)
X_test = X_test.reshape(X_test.shape[0], 1,28,28)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

#declare model 

model = Sequential()

#input layer
model.add(Conv2D(32, (3, 3), activation="relu", input_shape=(1, 28, 28), data_format="channels_first"))
print(model.output_shape)

#LEGO PHASE
model.add(Conv2D(32,3,3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

#compile model
model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

#fit model to the data
model.fit(X_train, Y_train, batch_size=32, nb_epoch=10, verbose=1)

#evaaaluations

score = model.evaluate(X_test, Y_test, verbose=0)