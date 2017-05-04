import numpy as np
import pickle

def parse(*categories):
    prefix = '../../data/um/all'
    with open(prefix + '.dta', 'rb') as dta, open(prefix + '.idx') as idx:
        names = {1: 'base', 2: 'valid', 3: 'hidden', 4: 'probe', 5: 'qual'}
        lists = {category: [] for category in categories}

        for i, (line, index) in enumerate(zip(dta, map(int, idx))):
            if i % 100000 == 0:
                print(i / (102000000) * 100)
            line = list(map(int, line.split()))
            cat = names[index]
            if cat in lists:
                lists[cat].append(line)
        print('Data separated.')

        for category, lst in lists.items():
            with open('{}.p'.format(category), 'wb') as file:
                pickle.dump(np.matrix(lst), file)
        print('Data pickled.')
