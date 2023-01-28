

weight = [0.1, 0.2, 0, 0.4]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    output = [a*b for a,b in zip(a,b)]
    return sum(output)

def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return print(prediction)

def vect_mat_x(vect, matrix):
    output = [0, 0, 0]
    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix)
    return output

ih_wgt = np.array([
[0.1, 0.2, -0.1], # hid[0]
[-0.1,0.1, 0.9], # hid[1]
[0.1, 0.4, 0.1]]).T # hid[2]])


hp_wgt = np.array([
[0.3, 1.1, -0.3], # hurt?
[0.1, 0.2, 0.0], # win?
[0.0, 1.3, 0.1] ]).T # sad?

weights = [ih_wgt, hp_wgt]

def np_neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[0])
    return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65,0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0], nfans[0]])

pred = np_neural_network(input, weights)

print(pred)












nt = [8.5, 9.5, 10, 9]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
weights = [0.1, 0.2, 0.0]
input = [toes[0], wlrec[0], nfans[0]]
#w_sum(nt, weight)
neural_network(input, weights)



