import numpy as np

x1 = 0.05
x2 = 0.10

np.random.seed(42)   

w1 = np.random.uniform(-0.5, 0.5)
w2 = np.random.uniform(-0.5, 0.5)
w3 = np.random.uniform(-0.5, 0.5)
w4 = np.random.uniform(-0.5, 0.5)
w5 = np.random.uniform(-0.5, 0.5)
w6 = np.random.uniform(-0.5, 0.5)


b1 = 0.5
b2 = 0.7


def tanh(x):
    return np.tanh(x)


h1_input = x1*w1 + x2*w2 + b1
h1 = tanh(h1_input)

h2_input = x1*w3 + x2*w4 + b1
h2 = tanh(h2_input)


output_input = h1*w5 + h2*w6 + b2
output = tanh(output_input)


print("Output of the Network =", output)
