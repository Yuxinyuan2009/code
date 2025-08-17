import tensorcircuit as tc
import numpy as np

def QFT(x):
    n = max(x) + 1
    m = len(x)
    c = tc.Circuit(n)
    for i in range(m):
        c.H(x[i])
        for j in range(i + 1, m):
            c.cphase(x[j], x[i], theta=np.pi / (2 ** (j - i)))
    for i in range(m // 2):
        c.swap(x[i], x[m - 1 - i])
    return c

