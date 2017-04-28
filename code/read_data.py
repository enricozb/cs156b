# Author: Bianca Yang

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import time
import math
import pickle
from sklearn.externals import joblib

NUM_USERS = 458292 
NUM_MOVIES = 17769

# Read in data
data = pd.read_csv('mu/all.dta', sep=' ', header=None, dtype=np.int32)
qual = pd.read_csv('mu/qual.dta', sep=' ', header=None, dtype=np.int32)
# splits = pd.read_csv('mu/all.idx', header=None, dtype=np.int32)
print('Got data.')

# Split data according to README
base = splits[splits[0] == 1].index.tolist()
valid = splits[splits[0] == 2].index.tolist()
hidden = splits[splits[0] == 3].index.tolist()

base_x = data.iloc[base, :-1]
base_y = data.iloc[base, -1]
valid_x = data.iloc[valid, :-1]
valid_y = data.iloc[valid, -1]
hidden_x = data.iloc[hidden, :-1]
hidden_y = data.iloc[hidden, -1]
print('Done splitting data.')

# Full data
# X = data.iloc[:, :-1]
# y = data.iloc[:, -1]

# Fit decision tree
clf = DecisionTreeRegressor(max_depth=200, min_impurity_split=1e-3)
clf.fit(base_x, base_y)
# clf.fit(X, y)
print('Done fitting data.') 

# Save model
joblib.dump(clf, 'tree.pkl')
print('Done saving model.')

# Predict on qual set.
# qpredict = np.array(clf.predict(qual))
# print('Done predicting qual.')
# np.savetxt('qsubmit.txt', qpredict, delimiter=' ')

# Predict on valid set. 
# print('Important features: '+str(clf.feature_importances_))
vpredict = np.array(clf.predict(valid_x))
valid_y = np.array(valid_y.values)
error = math.sqrt(sum((vpredict - valid_y)**2))
print(error)
# Error is 2000+
