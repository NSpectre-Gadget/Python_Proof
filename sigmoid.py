import numpy as np


#  Calc of activation function - a gate that checks that an incoming value is greater than a critical number
def sigmoid(w_sum):
    return 1 / (1 + np.exp(-w_sum))
