# Author: Bianca Yang

from read_data import *
import pickle as pkl
import json
import keras
from keras.models import model_from_json
import pandas as pd
import numpy as np

# Columns: user-movie-date-rating

# Read in non_probe and probe data 
non_probe = pd.read_csv('mu/non_probe.dta', sep=' ', header=None, \
        index_col=0)
probe = pd.read_csv('mu/probe.tab', sep='\t', header=0, index_col=0)
probe.columns= [1, 2, 3, 4]
non_qual = pd.concat([non_probe, probe])

# Treat 10% of probe as validation set. 
probe_val = probe.sample(frac=.1, axis=0)
probe_non_val = probe[~probe.isin(probe)].dropna()

# Features I'm going to create: 
# 1. How frequently each user rated movies
# 2. How frequently each movie got rated. 
# 3. How frequently ratings occured on each date. 
# 4. Neural network: enrico, github (part) 
# 5. Factor vectors from SVD: enrico, github. 
# 6. RBM hidden units 
# 7. Learn something based on time? 

print('Creating features.')
# 1 
# user_freq_dict = non_probe.groupby('user').count()['movie'].to_dict()
ufd_probe = non_qual.groupby(1).count()[2]
# with open('mu/user_freq_dict_probe.p', 'wb') as f:
#     pkl.dump(user_freq_dict_probe, f, protocol=pkl.HIGHEST_PROTOCOL)
# 
# # 2 
# movie_freq_dict = non_probe.groupby('movie').count()['user'].to_dict()
mfd_probe = non_qual.groupby(2).count()[1]
# with open('mu/movie_freq_dict_probe.p', 'wb') as f:
#     pkl.dump(movie_freq_dict_probe, f, protocol=pkl.HIGHEST_PROTOCOL)
# 

# 3
# rating_freq_date_dict = non_probe.groupby('date').count()['user'].to_dict()
rfd_probe = non_qual.groupby(3).count()[1]
# with open('mu/rating_freq_dict_probe.p', 'wb') as f:
#      pkl.dump(rating_freq_date_dict_probe, f, protocol=pkl.HIGHEST_PROTOCOL)

# Neural net predictions
# nnpred = 

# # # Combine non_probe
# # print('Combining non_probe.')
# # umd = non_probe.iloc[:, :3]
# # rat = non_probe.iloc[:, -1]
# # umd_tup = list(map(tuple, umd.values))
# # # Create UMD dictionary
# # UMD = dict(zip(umd_tup, rat.values))
# # 
# # # Combine everything.
# # UMDrat = {}
# # 
# # for key in UMD.keys(): 
# #     UMDrat[key] = (U[key[0]], M[key[1]], D[key[2]], UMD[key])
# # 
# # UMDrat_non = pd.DataFrame.from_dict(UMDrat, orient='index')
# # print('Writing non_probe.')
# # UMDrat_non.to_csv('mu/UMDrat_non_probe.dta', sep=' ', index_label=False)
# # # Write non_prob
# # # with open('mu/UMD_NN_rat_nonprob.p', 'wb') as f:
# # #     pkl.dump(out, f, protocol=pkl.HIGHEST_PROTOCOL)
# # 
# print('Combining probe.')
# Combine probe
umd = probe.iloc[:, :3]
rat = probe.iloc[:, -1]
umd_tup = list(map(tuple, umd.values))
# # Create UMD dictionary
UMD = dict(zip(umd_tup, rat.values))
# 
UMDrat = {}

# Read in SVD predictions
svd_pred = pd.read_csv(\
        '../cs156b/code/svd/predictions/saved/probe-K50-I100.dat', sep=' ', \
        header=None)
svd_pred.index = probe.index

numbers = list(probe.index)
i = 0
for key in UMD.keys(): 
    # UMDrat[key] = (U[key[0]], M[key[1]], D[key[2]])
    # UMDrat[key] = (ufd_probe[key[0]], mfd_probe[key[1]], rfd_probe[key[2]], UMD[key])
    UMDrat[numbers[i]] = (key[0], key[1], key[2], ufd_probe[key[0]], \
            mfd_probe[key[1]], rfd_probe[key[2]], UMD[key])
    i += 1

# Read in SVD matrices
user_50 = np.loadtxt('../cs156b/code/svd/predictions/matrices/U-K50-I100.mat')
user_50 = pd.DataFrame(user_50)
user_50.columns = user_50.columns.map(lambda x: str(x) + '_svd_u50')
movie_50 = np.loadtxt('../cs156b/code/svd/predictions/matrices/V-K50-I100.mat')
movie_50 = pd.DataFrame(movie_50)
movie_50.columns = movie_50.columns.map(lambda x: str(x) + '_svd_m50')

UMDrat_probe = pd.DataFrame.from_dict(UMDrat, orient='index')
UMDrat_probe.sort_index()
UMDrat_probe['svd_pred'] = svd_pred

UMDrat_probe = UMDrat_probe.join(user_50, on=0)
UMDrat_probe = UMDrat_probe.join(movie_50, on=1)

print('Writing probe w/o nn.')
UMDrat_probe.to_csv('mu/umd_umdfreq_rat_svd.dta', sep=' ', \
      index_label=False)

# 4
# print('Importing neural net.')
with open('../cs156b/code/deep/trained/3x64/3x64-dropout-base.a.json', \
        'rb') as json:
    model = model_from_json(pkl.load(json))
    model.load_weights('../cs156b/code/deep/trained/3x64/3x64-dropout-base.w.h5')
print('Done importing neural net.')

# Get the embedding layer weights. 
embedding = []
for l in model.layers[0].layers:
    embedding.append(l.get_weights()[0])
print('Done getting embedding layer weights.')

# User by 60
user_nn = pd.DataFrame(embedding[0])
user_nn.columns = user_nn.columns.map(lambda x: str(x) + '_nn_user')
UMDrat_probe = UMDrat_probe.join(user_nn, on=0)
# Movie by 60
movie_nn = pd.DataFrame(embedding[1])
movie_nn.columns = movie_nn.columns.map(lambda x: str(x) + '_nn_movie')
UMDrat_probe = UMDrat_probe.join(movie_nn, on=1)
# Date by 60 
date_nn = pd.DataFrame(embedding[2])
date_nn.columns = date_nn.columns.map(lambda x: str(x) + '_nn_date')
UMDrat_probe = UMDrat_probe.join(date_nn, on=2)

print('Writing probe w/ nn.')
UMDrat_probe.to_csv('mu/umd_umdfreq_rat_svd_nn.dta', sep=' ', \
      index_label=False)
# # Write probe
# # with open('mu/UMD_NN_rat_prob.p', 'w') as f:
# #     pkl.dump(out, f, protocol=pkl.HIGHEST_PROTOCOL)
# 
# # print('Combining non_qual.')
# # # Combine non_qual
# # umd = non_qual.iloc[:, :4]
# # rat = non_qual.iloc[:, -1]
# # umd_tup = list(map(tuple, umd.values))
# # # Create UMD dictionary
# # UMD = dict(zip(umd_tup, rat.values))
# # 
# # UMDrat = {}
# # for key in UMD.keys(): 
# #     UMDrat[key] = (U[key[0]], M[key[1]], D[key[2]], UMD[key])
# # 
# # 
# # UMDrat_non_qual = pd.DataFrame.from_dict(UMDrat, orient='index')
# # print('Writing non_qual.')
# # UMDrat_non_qual.to_csv('mu/UMDrat_non_qual.dta', sep=' ', index_label=False)
# # # Write non_qual
# # # with open('mu/UMD_NN_rat_nonqual.p', 'w') as f:
# # #     pkl.dump(out, f, protocol=pkl.HIGHEST_PROTOCOL)
# # 
# 




# 5

# 6

print('Done creating features.')
