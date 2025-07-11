import numpy as np

def f(x):
    res = 0.
    for i in range(len(x)):
        res += x[i] * x[i]
    return np.float64(res)

delta = 1e-5

def derivative(x):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_array = x.copy()
        x_array[i] += delta
        t = f(x_array)
        x_array[i] -= 2.*delta
        grad[i] = (t - f(x_array)) / (2. * delta)
    return grad

print(derivative(np.array([1., 2.])))
