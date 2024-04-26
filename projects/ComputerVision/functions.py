import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import cv2 as cv

def resize(img, size):
    return cv.resize(img, size)

def get_image_data(fnames):
    image_data = []
    for i in range(len(fnames)):
        data = resize(cv.imread(fnames[i]), (224, 224))
        image_data.append(data)
    return image_data