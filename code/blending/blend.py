# Blending, featuring Linear Regression
# Claire Goeckner-Wald

import numpy as np

# receives [filenames of model outputs to train on]
# returns [linear coefficients of each model, in order they were passed in]
# N is the number of points that the algorithm is trained on
def linear_regression(filenames):

	# Get probe training & testing data
	probe_data = get_probe_data()
    # to minimize E_in, find w = psuedo-inverse of x * y
    weight_vector = np.dot(np.linalg.pinv(data_points), y)

    # return the weight vector, too, for problem #6
    return (weight_vector)

# returns probe data from known file location
def get_probe_data(file=""):


def blend(filenames, type="linear_regression")
	return linear_regression(filenames)











# Return coefficients on each model