import pandas as pd
import os
import opendatasets as od
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import cv2 as cv
import random as rnd

def get_class_directories():
    fish = os.listdir('jellyfish-types')
    class_directories = []
    for category in fish:
        class_directories = class_directories + ['jellyfish-types/{}/'.format(category)]
    return class_directories

def get_jpgs():
    jpgs = []
    for cd in get_class_directories():
        for i in range(len(os.listdir(cd))):
            jpgs.append(cd + os.listdir(cd)[i])
    return jpgs

def get_labels():
    labels = []
    jpgs = get_jpgs()
    for i in range(len(jpgs)):
        if 'compass' in jpgs[i]:
            labels.append('compass')
        elif 'Moon' in jpgs[i]:
            labels.append('Moon')
        elif 'blue' in jpgs[i]:
            labels.append('blue')
        elif 'lions_mane' in jpgs[i]:
            labels.append('lions_mane')
        elif 'barrel' in jpgs[i]:
            labels.append('barrel')
    return labels

def resize(img, size):
    return cv.resize(img, size)

def get_pixel_means():
    jpgs = get_jpgs()
    means = []
    for i in range(len(jpgs)):
        img_data = plt.imread(jpgs[i])
        img_data = resize(img_data, (224, 224))
        means.append(np.mean(np.mean(img_data, axis = 1), axis = 0))
    return pd.DataFrame(means, columns = ['r_means', 'g_means', 'b_means'])

def rgb_mean_outliers(r_means, g_means, b_means):
    rmean, gmean, bmean = r_means.mean(), g_means.mean(), b_means.mean()
    rstd, gstd, bstd = np.std(r_means), np.std(g_means), np.std(b_means)
    threshold = 3
    r_outliers, g_outliers, b_outliers = [], [], []
    r_indexes, g_indexes, b_indexes = [], [], []
    for i in range(len(r_means)):
        rz_score = (r_means[i] - rmean) / rstd
        gz_score = (g_means[i] - gmean) / gstd
        bz_score = (b_means[i] - bmean) / bstd
        if abs(rz_score > threshold):
            r_outliers.append(r_means[i])
            r_indexes.append(i)
        if abs(gz_score > threshold):
            g_outliers.append(g_means[i])
            g_indexes.append(i)
        if abs(bz_score > threshold):
            b_outliers.append(b_means[i])
            b_indexes.append(i)
    return r_outliers, r_indexes, g_outliers, g_indexes, b_outliers, b_indexes

def edge_density():
    jpgs = get_jpgs()
    densities = []
    for i in range(len(jpgs)):
        img = cv.imread(jpgs[i], cv.IMREAD_GRAYSCALE)
        img = resize(img, (224, 224))
        assert img is not None, "file could not be read, check with os.path.exists()"
        edges = cv.Canny(img, 50, 150)
        edge_counts = np.sum(edges > 0)
        edge_density = edge_counts / (edges.shape[0] * edges.shape[1])
        densities.append(edge_density)
    return densities

def density_outliers(densities):
    mean = np.mean(densities)
    std = np.std(densities)
    threshold = 3
    outliers = []
    indexes = []
    for i in range(len(densities)):
        z_score = (densities[i] - mean) / std
        if abs(z_score) > threshold:
            outliers.append(densities[i])
            indexes.append(i)
    return outliers, indexes

def get_imgs():
    imgs = []
    for cd in get_class_directories():
        for i in range(100):
            imgs.append(cd + os.listdir(cd)[i])
    return imgs

def get_target():
    target = []
    imgs = get_imgs()
    for i in range(len(imgs)):
        if 'compass' in imgs[i]:
            target.append('compass')
        elif 'Moon' in imgs[i]:
            target.append('Moon')
        elif 'blue' in imgs[i]:
            target.append('blue')
        elif 'lions_mane' in imgs[i]:
            target.append('lions_mane')
        elif 'barrel' in imgs[i]:
            target.append('barrel')
    return target

def get_x_data():
    imgs = get_imgs()
    x = []
    for i in range(len(imgs)):
        img_data = resize(cv.imread(imgs[i]), (224, 224))
        x.append(img_data)
    return np.asarray(x)