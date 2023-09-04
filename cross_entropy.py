import numpy as np


# Loss Function
def cross_entropy(target, pred):
    return -(target * np.log10(pred) + (1 - target) * (np.log10(1 - pred)))
