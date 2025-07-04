import tensorcircuit as tc
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la
import math

K = tc.set_backend("tensorflow")
I = tc.gates._i_matrix
X = tc.gates._x_matrix
Y = tc.gates._y_matrix
Z = tc.gates._z_matrix
n = int(input())
A = np.zeros(2**n)

for i in range(1, n+1):
    if i == 1:
        U = Z
    else: 
        U = I
    for j in range(2, n+1):
        if j == i:
            W = Z
        else:
            W = I
        U = np.kron(U, W)
    A = A + U
for i in range(1, n):
    if i == 1:
        U = X
    else:
        U = I
    for j in range(2, n+1):
        if j == i or j == i + 1:
            W = X
        else:
            W = I
        U = np.kron(U, W)
A = A + U
v = np.array([0]*(2**n))
v[0] = 1
print(v)
print(v @ A @ v.conj().T)
