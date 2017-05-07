# Blending, featuring Linear Regression
# Claire Goeckner-Wald

import numpy as np
import pickle

# receives [filenames of model outputs to train on]
# returns [linear coefficients of each model, in order they were passed in]
# N is the number of points that the algorithm is trained on
def linear_regression(filenames):
	# print(get_data(filenames[0]))
	# return

	# Get probe data (filepath is known)
	probe_y = np.matrix(get_data(filename="../../data/um/probe.dta", filetype="probe")).T

	# Get the model data
	# Each model file is a 1-by-N prediction on probe.dta
	model_data = []
	for file in filenames:
		# Combine the models into a matrix
		model_data.append(get_data(file, filetype="model"))
	model_data = np.matrix(model_data).T
	# Print model_data
	# np.savetxt(fname="model_data.dta", X=model_data[][:500])
	# return

	# to minimize Error_in, find w = psuedo-inverse of x * y
	# Weight vector will be a list of linear coefficients of the models, in order of receipt
	weight_vector = list(np.dot(np.linalg.pinv(model_data), probe_y))

	# Return the weight vector 
	return list(map(float, weight_vector))

# returns probe data from known file location
def get_data(filename, filetype):
	with open(filename) as file:
		# Return a list for probe
		if filetype == "probe":
			return [int(line.strip().split()[-1]) for line in file]
		# Return a list
		elif filetype == "model":
			return [float(line.strip().split()[-1]) for line in file]
		# User error
		else:
			return -1

# Return linear coefficients on each model
def blend(filenames, blend_type="linear_regression"):
	if blend_type == "linear_regression":
		return linear_regression(filenames)
	return -1

print(blend(["test.dta", "test.dta"]))
