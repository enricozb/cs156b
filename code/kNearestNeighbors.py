# Implements k-Nearest Neighbors with sklearn
# Claire Goeckner-Wald

from sklearn.neighbors import NearestNeighbors
import numpy as np
from python_parse import get

k = 3

trainX = get("trainX.txt")
trainY = get("trainY.txt")

# Valid algorithm arguments: ['auto', 'ball_tree', 'kd_tree', 'brute']
# When the default value 'auto' is passed, the algorithm attempts to 
# determine the best approach from the training data.

# Default:
# NearestNeighbors(n_neighbors=5, radius=1.0, algorithm='auto', leaf_size=30, metric='minkowski', p=2, metric_params=None, n_jobs=1, **kwargs)

model = NearestNeighbors(n_neighbors=k, algorithm='auto')

model.fit(zip(trainX, trainY))



