import tensorcircuit as tc
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la
import math

K = tc.set_backend("tensorflow")

X = tc.gates._x_matrix
Y = tc.gates._y_matrix
Z = tc.gates._z_matrix

def ma(t):
    if t == 0:
        return X
    elif t == 1:
        return Y
    else:
        return Z
print("abc")
a = int(input())
b = int(input())
theta = float(input())

def f(a, b, theta):
    P = ma(a)
    Q = ma(b)
    u = np.array([1, 0])
    v = la.expm(theta * 0.5j * P) @ u
    return v.conj().T @ Q.conj().T @ v

def derivative():
    t = f(a, b, theta + math.pi/2.)
    s = f(a, b, theta - math.pi/2.)
    grad = (t - s)/2
    return K.real(grad)

print(derivative())
