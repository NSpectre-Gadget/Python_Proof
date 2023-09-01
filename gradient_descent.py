import numpy as np

def sigmoid(w_sum):
    return 1/(1+np.exp(-w_sum))

#Get Model Output
def get_prediction(features, weights, bias):
    return sigmoid(np.dot(features, weights) + bias)

#Loss Function
def cross_entropy(target, pred):
    return -(target*np.log10(pred)+(1-target)*(np.log10(1-pred)))

# how to update weights in a perceptron 
def gradient_descent(feature, weights, target, prediction, l_rate, bias):
    ''' 
    argument data types:
        feature, weights = lists with 3 items
        target = integer (0 or 1)
        prediction, 1_rate, bias = floating point numbers
    retuns(tuple):
            new weights, new bias
    '''
    new_weights = []
    bias += l_rate*(target-prediction)
    for x, w in zip(feature, weights):
        new_w = w + l_rate*(target - prediction) * x
        new_weights.append(new_w)
    return new_weights, bias

#Data
features = np.array(([0.1, 0.5, 0.2], [0.2, 0.3, 0.1], [0.7, 0.4, 0.2], [0.1, 0.4, 0.3]))
targets = np.array([0, 1, 0, 1])
weights = np. array([0.4, 0.2, 0.6])
bias = 0.5
l_rate = 0.1
e=2.71828
