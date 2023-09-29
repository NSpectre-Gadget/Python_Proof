import matplotlib.pyplot as plt

# import numpy as np
# import pandas as pd
from nn_datageneration import generate_data
from sigmoid import sigmoid
from cross_entropy import cross_entropy
from updated_weights import updated_weights
from get_weighted_sum import get_weighted_sum
from update_bias import update_bias

bias = 0.5
l_rate = 0.1
epochs = 10
epoch_loss = []

data, weights = generate_data(4, 3)


def train_model(data, weights, bias, l_rate, epochs):
    for e in range(epochs):
        individual_loss = []
        for i in range(len(data)):
            feature = data.loc[i][:-1]
            target = data.loc[i][-1]
            w_sum = get_weighted_sum(feature, weights, bias)
            prediction = sigmoid(w_sum)
            loss = cross_entropy(target, prediction)
            individual_loss.append(loss)
            print("Old Values")
            # gradient descent
            print(weights, bias)
            weights = updated_weights(weights, l_rate, target, prediction, feature)
            bias = update_bias(bias, l_rate, target, prediction)
            print("New Values")
            print(weights, bias)

        average_loss = sum(individual_loss) / len(individual_loss)
        epoch_loss.append(average_loss)
        print("********************")
        print("epoch", e)
        print(average_loss)


train_model(data, weights, bias, l_rate, epochs)


# (features * weights) + bias
# get_weighted_sum()


# sigmoid()

# cross_entropy()

# updated_weights()


# update_bias()
# np.epoch([0, 6])
# plot the average loss
# df = pd.DataFrame(epoch_loss)
# df_plot = df.plt(kind="line", grid=True).get_figure()
# df_plot.savefig("training_Loss.pdf")
