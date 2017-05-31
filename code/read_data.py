# Author: Bianca Yang
# Last edited: May 4, 2017

# Some functions for reading in data and splitting it according to the readme. 

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import time
import math
import pickle
from sklearn.externals import joblib

NUM_USERS = 458292 
NUM_MOVIES = 17769

def read_data(ixcol, hd, file=None, separator=','):
    print('\nGetting data.')
    data = pd.read_csv(file, sep=separator, header=hd, index_col=ixcol)
    print('Done getting data.')
    return data

def split_data_readme(splits, data):
    print('\nSplitting data.')
    base_ix = splits[splits[0] == 1].index.tolist()
    valid_ix = splits[splits[0] == 2].index.tolist()
    hidden_ix = splits[splits[0] == 3].index.tolist()
    probe_ix = splits[splits[0] == 4].index.tolist()
    non_probe_ix = splits[splits[0] != 4]
    non_probe_ix = non_probe_ix[non_probe_ix[0] != 5].index.tolist()

    base = data.iloc[base_ix]
    valid = data.iloc[valid_ix]
    hidden = data.iloc[hidden_ix]
    probe = data.iloc[probe_ix]
    non_probe = data.iloc[non_probe_ix] 
    
    print('Done splitting data.')
    return base, valid, hidden, probe, non_probe

def write_splits_space(df, fname):
    '''Writes a dataframe df to a file.'''
    print('\nWriting data.')
    df.to_csv('mu/{0}.dta'.format(fname), sep=' ', header=['user', \
            'movie', 'date', 'rating'])
    print('Done writing space-separated data.')

def write_splits_orange(df, fname):
    # Create additional rows to make Orange happy 
    print('\nWriting tab-separated data.')
    df.to_csv('mu/{0}.tab'.format(fname), sep='\t', header=['user', \
            'movie', 'date', 'rating'])
    print('Done writing tab-separated data.')

def main(): 
    data = read_data(None, None, file='mu/all.dta', separator=' ')
    splits = read_data(None, None, file='mu/all.idx', separator=' ')
    base, valid, hidden, probe, non_probe = split_data_readme(splits, data)
    # write_splits_space(base, 'base')
    # write_splits_space(valid, 'valid')
    # write_splits_space(hidden, 'hidden')
    # write_splits_space(probe, 'probe')
    # write_splits_space(non_probe, 'non_probe')

    # base.loc[-1] = ['continuous', 'continuous', 'time', 'continuous']
    # base.loc[-2] = ['row=1', 'col=1', 'meta', 'class']
    # base.index = base.index + 2
    # base = base.sort_index()

    # valid.loc[-1] = ['continuous', 'continuous', 'time', 'continuous']
    # valid.loc[-2] = ['row=1', 'col=1', 'meta', 'class']
    # valid.index = valid.index + 2
    # valid = valid.sort_index()

    # hidden.loc[-1] = ['continuous', 'continuous', 'time', 'continuous']
    # hidden.loc[-2] = ['row=1', 'col=1', 'meta', 'class']
    # hidden.index = hidden.index + 2
    # hidden = hidden.sort_index()

    # probe.loc[-1] = ['continuous', 'continuous', 'time', 'continuous']
    # probe.loc[-2] = ['row=1', 'col=1', 'meta', 'class']
    # probe.index = probe.index + 2
    # probe = probe.sort_index()

    non_probe.loc[-1] = ['continuous', 'continuous', 'time', 'continuous']
    non_probe.loc[-2] = ['row=1', 'col=1', 'meta', 'class']
    non_probe.index = non_probe.index + 2
    non_probe = non_probe.sort_index()

    # write_splits_orange(base, 'base')
    # write_splits_orange(valid, 'valid')
    # write_splits_orange(hidden, 'hidden')
    # write_splits_orange(probe, 'probe')
    write_splits_orange(non_probe, 'non_probe')

if __name__ == '__main__':
    main()
