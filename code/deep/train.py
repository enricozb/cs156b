import numpy as np
import pickle
import tensorflow as tf

from keras.models import Sequential, Model
from keras.layers.core import Dense, Activation, Flatten, Dropout
from keras.layers.embeddings import Embedding
from keras.layers import Merge

with open('base.p', 'rb') as base, open('valid.p', 'rb') as valid, \
    open('probe.p', 'rb') as probe:

    tr = pickle.load(base)
    tr = np.concatenate((tr, pickle.load(probe)))

    ts = pickle.load(valid)

L = len(tr)
M = len(ts)

print("Data loaded.")

movie_count = 17771
user_count = 458294
date_count = 2244

model_user = Sequential()
model_user.add(Embedding(user_count, 60, input_length=1))

model_movie = Sequential()
model_movie.add(Embedding(movie_count, 60, input_length=1))

model_date = Sequential()
model_date.add(Embedding(date_count, 1, input_length = 1))

model = Sequential()
model.add(Merge([model_user, model_movie, model_date], mode='concat'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(64, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adadelta')

print("Model complete.")

model.fit([tr[:,0].reshape(L,1), tr[:,1].reshape(L,1), tr[:,2].reshape(L, 1)],\
    tr[:,3].reshape(L,1), batch_size=24000, epochs=42,\
    validation_data=([ ts[:,0].reshape(M,1),\
        ts[:,1].reshape(M,1),ts[:,2].reshape(M, 1)], ts[:,3].reshape((M,1))))

print("Trained.")

with open('model.a.json', 'wb') as json:
    pickle.dump(model.to_json(), json)
    model.save_weights('model.w.h5')

with open('qual.p', 'rb') as qual:
    qual = pickle.load(qual)

L = len(qual)
X = [qual[:,0].reshape(L,1), qual[:,1].reshape(L,1), qual[:,2].reshape(L, 1)]

with open('prediction.txt', 'w') as pr:
    prediction = model.predict(X)
    for p in prediction:
        pr.write('{:.2f}\n'.format(float(p)))
