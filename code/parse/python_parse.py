# File contains a helper function to parse the datasets
# Claire Goeckner-Wald 

# Gets the data from a file called "filename"
# Returns the data as a list of lists of integers,
# for example, a file containing "1 2 3\n4 5 6" will return
# [[1, 2, 3],[4, 5, 6]]
def get(filename):
	lst = []
	with open(filename) as file:
		for line in file:
			lst.append(list(map(int, line.strip().split())))

	return lst