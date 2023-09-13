def update_bias(bias, l_rate, target, prediction):
    return bias + l_rate * (target - prediction)
