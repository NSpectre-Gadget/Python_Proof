import math
# Features
# Weighted_sum
# y = target
# y_hat = predicted

# This program takes the features weighted sum and target comparison
# and calculates the loss to ultimately find the coross entry loss so 
# so there is a penalty for applied to incorrect classified inputs/features

input_data = [(.26, 1), (.20, 0), (.48, 1), (.30, 0)]

def cross_entropy(input_data):
    loss=0
    n=len(input_data)
    for entry in input_data:
        w_sum = entry[0]
        y=entry[1]

        loss += -(y*math.log10(w_sum)+ (1-y)*math.log10(1-w_sum))
        print(-(y*math.log10(w_sum)+ (1-y)*math.log10(1-w_sum)))
    return loss/n

error_term = cross_entropy(input_data)
print(error_term)