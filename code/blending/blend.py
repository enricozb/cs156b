# Blending, featuring Linear Regression
# Claire Goeckner-Wald

import numpy as np

# receives [filenames of model outputs to train on]
# returns [linear coefficients of each model, in order they were passed in]
# N is the number of points that the algorithm is trained on
def linear_regression(filenames):

	# Get probe data (filepath is known)
	probe_data = get_data(filename="../../data/um/probe.dta")

	# Retrieve the correct probe classifications (third column)
	_, _, probe_y = zip(*probe_data)

	# Get the model data
	model_data = []
	for file in filenames:
		model_data.append(file.readlines())

	# to minimize Error_in, find w = psuedo-inverse of x * y
	# Weight vector will be a list of linear coefficients of the models, in order of receipt
	weight_vector = list(np.dot(np.linalg.pinv(data_points), y))

	# Return the weight vector 
	return weight_vector

# returns probe data from known file location
def get_data(filename):
	with open(filename) as file:
		return file.readlines()

# Return linear coefficients on each model
def blend(filenames, blend_type="linear_regression"):
	if blend_type == "linear_regression":
		return linear_regression(filenames)
	return -1

print(blend(["test.dta"]))
