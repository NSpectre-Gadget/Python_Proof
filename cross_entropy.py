import numpy as np


# Loss Function - measuring the contrast between two random variables.
def cross_entropy(target, pred):
    return -(target * np.log10(pred) + (1 - target) * (np.log10(1 - pred)))
