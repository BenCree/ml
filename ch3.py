##2
weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001
output = input * weight
# naive implementation
for iteration in range(1101):
    error = (weight*input - goal_prediction)
    if error > 0 and abs(error) > 0.000001:
        input = input - step_amount
        output = weight*input
        print('too high, lowering : output = ', output)
    elif error < 0 and abs(error) > 0.000001:
        input = input + step_amount
        output = weight*input
        print('too low, raising : output = ', output)
    else:
        print(f'converged: input = {input}, output = {output}')

# classic implementation
for iteration in range(20):
    pred = input*weight
    error = (pred - goal_pred)**2
    delta = pred - goal_pred
    weight_delta = input*delta
    weight = weight + (weight_delta*alpha)













weight = 0.4
input = 0.5
alpha = 0.1
goal_pred = 8

for iteration in range(20):
    pred = weight * input
    error = (pred - goal_pred)**2
    derivative = input * (pred - goal_pred)
    weight = weight + (derivative * alpha)


