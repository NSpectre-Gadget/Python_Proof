x_input=[0.1, 0.5, 0.2] #factors considered
w_weights=[0.4, 0.3, 0.6] # weight given to each factor
threshold=0.5
#using a threshold instead of applying bias to each weighted input
def step(weighted_sum):
    if weighted_sum > threshold:
        return 1
    else:
        return 0
    
def perceptron():
    weighted_sum=0
    for x,w in zip(x_input, w_weights):
        weighted_sum+=x*w
        print(weighted_sum)
    return step(weighted_sum)

output=perceptron()
print("output: " + str(output))