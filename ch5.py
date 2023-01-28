from ch2 import np_neural_network, w_sum, vect_mat_x
# predicting multiple outputs from one input
weights = [0.3, 0.2, 0.9]

def ele_mul(vec1, vec2):
    result = [a*b for a, b in vec1, vec2]
    return result

def neural_network(input, weights):
    pred = ele_mul(input,weights)
    return pred

wlrec = [0.65, 1.0, 1.0, 0.9]

hurt  = [0.1, 0.0, 0.0, 0.1]
win   = [  1,   1,   0,   1]
sad   = [0.1, 0.0, 0.1, 0.2]
# set input and truth
input = wlrec[0]
true = [hurt[0], win[0], sad[0]]


pred = neural_network(input, weights)

error = [0, 0, 0]
delta = [0, 0, 0]
# calculate errors and deltas for each element
for i in range(len(error)):
    error[i] = (pred[i] - true[i])**2
    delta[i] = pred[i] - true[i]

def scalar_ele_mul(number, vector):
    output = [0, 0, 0]
    assert len(number) == len(vector)
    for i in range(len(number)):
        output[i] += number * vector[i]
    return output

weight_deltas = scalar_ele_mul(input, delta)

alpha = 0.1

# update weights
for i in range(len(weights)):
    weights[i] += (weights_deltas[i] * alpha)



