import tensorcircuit as tc
import numpy as np
from add import *

def add_const(x, t):
    '''
    |x> -> |x+c(mod 2**n)>
    '''
    c = tc.Circuit(max(x) + 1)
    n = len(x)
    c.append(QFT(x))
    for j in range(n):
        if t>>(3 - j) & 1:
            for i in range(n - 1 - j, n):
                c.phase(x[i], theta=np.pi / (2 ** (i + j - n + 1)))
    c.append(QFT(x).inverse())
    return c

def cadd_const(p, x, t):
    c = tc.Circuit(max(x + [p]) + 1)
    n = len(x)
    c.append(QFT(x))
    for j in range(n):
        if t>>(3 - j) & 1:
            for i in range(n - 1 - j, n):
                c.cphase(p, x[i], theta=np.pi / (2 ** (i + j - n + 1)))
    c.append(QFT(x).inverse())
    return c

def ccadd_const(p, q, x, t):
    c = tc.Circuit(max(x + [p, q]) + 1)
    n = len(x)
    c.append(QFT(x))
    for j in range(n):
        if t>>(3 - j) & 1:
            for i in range(n - 1 - j, n):
                c.append(ccphase(p, q, x[i], theta=np.pi / (2 ** (i + j - n + 1))))
    c.append(QFT(x).inverse())
    return c
