import tensorcircuit as tc
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la

K = tc.set_backend("tensorflow")

X = tc.gates._x_matrix
Y = tc.gates._y_matrix
print(la.expm(X))
print(la.expm(Y))
print(X @ Y)
print(la.expm(X @ Y))
