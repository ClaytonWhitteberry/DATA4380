import pandas as pd
import numpy as np
import pyarrow
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy
from scipy import signal
import antropy as ant


def standardize(sub_eeg):
    standard = StandardScaler()
    return pd.DataFrame(standard.fit_transform(sub_eeg), columns = sub_eeg.columns)

def replace_nulls(sub_eeg):
    for col in sub_eeg.columns:
        if pd.isnull(sub_eeg).sum().sum() > 0:
            sub_eeg[col].fillna(sub_eeg[col].median(), inplace = True)
    return sub_eeg

def get_sub_eeg(data, row):
    eeg_id = str(data['eeg_id'][row])
    eeg_parquet = eeg_id + '.parquet'
    eeg = pd.read_parquet('train_eegs/' + eeg_parquet, engine = 'pyarrow')
    starting_row = int(data['eeg_label_offset_seconds'][row] * 200)
    ending_row = int(starting_row + 10000)
    sub_eeg = eeg.iloc[starting_row: ending_row]
    sub_eeg = sub_eeg.reset_index()
    sub_eeg = sub_eeg.drop(columns = 'index')
    return sub_eeg

def preprocess(sub_eeg):
    sub_eeg = replace_nulls(sub_eeg)
    sub_eeg = standardize(sub_eeg)
    return sub_eeg

def welch(data):
    f_list = []
    pxx_list = []
    for col in data.columns:
        f, pxx = signal.welch(data[col], fs = 200)
        f_list.append(f)
        pxx_list.append(pxx)
    return f_list, pxx_list

def principal_components(data, n):
    pca_cols = ['component{}'.format(i + 1) for i in range(n)]
    pca = PCA(n_components = n)
    pca.fit(data)
    pca_eeg = pca.transform(data)
    return pd.DataFrame(pca_eeg, columns = pca_cols)

def get_band_features(f, pxx):
    alpha_band = [8, 12]
    beta_band = [12, 30]
    alphas, betas = [], []
    for i in range(len(f)):
        a = np.trapz(pxx[i][(f[i] >= alpha_band[0]) & (f[i] <= alpha_band[1])], f[i][(f[i] >= alpha_band[0]) & (f[i] <= alpha_band[1])])
        b = np.trapz(pxx[i][(f[i] >= beta_band[0]) & (f[i] <= beta_band[1])], f[i][(f[i] >= beta_band[0]) & (f[i] <= beta_band[1])])
        alphas.append(a)
        betas.append(b)
    return alphas, betas

def mobility_complexity(data):
    mobs, coms = [], []
    for col in data.columns:
        mob, com = ant.hjorth_params(data[col])
        mobs.append(mob)
        coms.append(com)
    return mobs, coms