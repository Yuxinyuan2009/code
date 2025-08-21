import numpy as np

def f(x):
    res = 0.
    for i in range(len(x)):
        res += x[i] * x[i]
    return np.float64(res)

delta = 0.001

def derivative(x):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_array = x.copy()
        x_array[i] += delta
        grad[i] = (f(x_array) - f(x)) / delta
    return grad

print(derivative(np.array([1., 2.])))
