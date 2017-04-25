# Implements Boltzmann Machine with sklearn
# Claire Goeckner-Wald

from sklearn.neural_network import BernoulliRBM
import numpy as np
from python_parse import get

# RBM = Restricted Boltzmann Machine

trainX = get("trainX.txt")
trainY = get("trainY.txt")

# Default values:
# BernoulliRBM(n_components=256, learning_rate=0.1, batch_size=10, n_iter=10, verbose=0, random_state=None)[source]¶

model = BernoulliRBM(random_state=0, verbose=True)

model.fit(zip(trainX, trainY))
