# -*- coding: utf-8 -*-
"""Homework_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xIvuXwl0Tip-ayEhqoXG5SRaJhY_cxRm

# Design Choices in Recurrent Neural Networks

###  Importing packages
"""

import re
import numpy as np
import pandas as pd 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.datasets import imdb

from keras.utils.np_utils import to_categorical

import warnings
warnings.filterwarnings('ignore')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

"""### Preparing Dataset"""

max_features = 1000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

# save np.load
#np_load_old = np.load

# modify the default parameters of np.load
#np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

#np.load = np_load_old

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

"""## Part 1: Influence of number of nodes

Try the models with different number of nodes such as 32, 64, 128 etc.

Analyze the number of model parameters, accuracy and training time

### LSTM with 8 nodes
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 8))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### LSTM with 16 nodes"""

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here 
# 
# # Use the same layer design from the above cell 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 8))
# model.add(LSTM(16, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 8))
# model.add(LSTM(128, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### Write your findings about number of nodes here?

1.   Finding 1
2.   Finding 2

1.   Finding 1: Increasing the number of nodes to 8, increased the accuracy, however increasing the nodes to 128 actually reduced accuracy.
2.   Finding 2: Increasing the number of nodes was directly related to time taken for the model, which makes sense as more nodes means more computation.

## Part 2: Influence of Embedding
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 4))
# model.add(LSTM(16, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 2))
# model.add(LSTM(16, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 32))
# model.add(LSTM(16, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### Write your findings about number of embedding features here?

1.   Finding 1
2.   Finding 2

1.   Finding 1: Decreasing or increasing the embedding features has no general effect on accuracy, it remains fairly same.
2.   Finding 2: Decreasing embedding features to 2 decreased the time, however increasing them to 32 took less time than with 4 features, which was unexpected.

## Part 3: Influence of Dropout

Try the models with different rates of dropout from 0 to 1

Analyze the number of model parameters, accuracy and training time

### Dropout with rate 0.5
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 32))
# model.add(LSTM(8, dropout=0.5, recurrent_dropout=0.5))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 32))
# model.add(LSTM(8, dropout=0.7, recurrent_dropout=0.3))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 32))
# model.add(LSTM(8, dropout=0.3, recurrent_dropout=0.7))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### Write your findings about influence of dropout rate here?

1.   Finding 1
2.   Finding 2

1.   Finding 1: Dropout did not have any general effect on accuracy of model.
2.   Finding 2: Dropout ratios had an effect on the time taken for the model, where when the dropout ratios were different from each other, the time taken decreased.

## Part 4: Multilayered RNNs

Try the models with different number of layers from smaller to larger.

Analyze the number of model parameters, accuracy and training time

### RNN with 2 layer LSTM
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 8))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0, return_sequences=True))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0, return_sequences=True))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### RNN with 3 layer LSTM"""

# Commented out IPython magic to ensure Python compatibility.
# # Write your code here. Use the same architecture as above. 
# 
# %%time
# 
# model = Sequential()
# model.add(Embedding(max_features, 8))
# model.add(LSTM(8, dropout=0.3, recurrent_dropout=0.7, return_sequences=True))
# model.add(LSTM(8, dropout=0.7, recurrent_dropout=0.3, return_sequences=True))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0, return_sequences=True))
# model.add(LSTM(8, dropout=0.0, recurrent_dropout=0.0))
# model.add(Dense(1, activation='sigmoid'))
# model.summary()
# 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=batch_size, epochs=1, validation_data=(x_test, y_test))
# 
# score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)

"""### Write your findings about number of layers here?

1.   Finding 1
2.   Finding 2

1.   Finding 1: Increasing one layer caused the accuracy to decrease, which was expected as because the number of layers increased, the process of back propogation becomes inefficient. 
2.   Finding 2: The time taken almost doubled with the addition of just one layer, which explains how much one layer can effect an RNN.
"""