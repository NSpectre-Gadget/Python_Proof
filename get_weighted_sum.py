import numpy as np


def get_weighted_sum(feature, weights, bias):
    return np.dot(feature, weights) + bias
