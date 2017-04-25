# Author: Michelle
import numpy as np

# 458,293 users, 1-indexed,
# 17,770 movies, 1-indexed.
# Ratings are between 1 and 5. (0 ratings are blanked out test data)
NUM_USERS = 458293
NUM_MOVIES = 17770

# Format of each line in all.dta:
# (user number)       (movie number)       (date number)       (rating)
# Format of each line in qual.dta:
# (user number)       (movie number)       (date number)

# Returns X and Y as numpy matrices. Excludes test set.
# sort_order um: X is sorted by users first then movies
#            mu: X is sorted by movies first then users
# name: all for all.dta
#       qual for qual.dta
def get(sort_order, name='all'):
    X = []
    y = []

    data = open('../../data/'+sort_order+'/'+name+'.dta', 'r')

    while True:
        s = data.readline()
        if not s:
            break

        user, movie, _, rating = map(int, s.split()) # is int ok??

        # ignore blanked out ratings (test set)
        if rating == 0: 
            continue

        X.append([user, movie])
        y.append(rating) # TODO how are duplicate entries dealt with?
    
    data.close()

    return np.matrix(X), np.array(y)

def get_data():
    # for svm
    # returns x, y
    pass

def load_data():
    # maybe?
    return X, y

def save_data(X, y):
    return 