# Author: Michelle
import numpy as np
import data_io

# SGDClassifier with hinge loss equivalent to linear-kernel SVM
# http://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-unbalanced-py
# and also because we're building a composite model anyway
from sklearn.linear_model import SGDClassifier
# using it because of the large number of data points

# Tests with a random selection of all points.
def test_in_sample(clf, X, y, fraction=0.01):
    num_pts = len(X)
    test_indices = np.random.choice(num_pts, size=int(num_pts*fraction), replace=False)
    
    test_X = X[test_indices]
    test_y = y[test_indices]
    
    predicted_y = np.round(clf.predict(test_X))#map(int, np.round(clf.predict(X)))
    
    # compare predicted and actual y
    print('Percent of exactly correct predictions: ' + str(np.count_nonzero(test_y==predicted_y)/len(test_y) * 100.0))
    # TODO get a real loss function in here

    return test_y, predicted_y

# Tests using the probe test points.
def test_probe(clf):
    pass # TODO

def predict():
    pass

X, y = data_io.get('um')

clf = SGDClassifier(loss='hinge', n_iter=100, alpha=0.01)
clf.fit(X, y)

yt, yp = test_in_sample(clf, X, y)