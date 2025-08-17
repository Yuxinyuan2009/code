import tensorcircuit as tc
import numpy as np
from QFT import *
from base import *

def add(x, y):
    '''
    |x>|y> -> |x>|x+y(mod 2**n)>
    '''
    c = tc.Circuit(max(x + y) + 1)
    n = len(y)
    c.append(QFT(y))
    for i in range(n):
        for j in range(n - 1 - i, n):
            c.cphase(x[i], y[j], theta=np.pi / (2 ** (i + j - n + 1)))
    c.append(QFT(y).inverse())
    return c

# 测试示例
'''
for i in range(16):
    for j in range(16):
        c = tc.Circuit(8)
        c.append(set(i, [0, 1, 2, 3]))
        c.append(set(j, [4, 5, 6, 7]))
        c.append(add([0, 1, 2, 3], [4, 5, 6, 7]))
        print(f"{i} + {j} = ", end="")
        out(c.state())
        print()
'''

def cadd(p, x, y):
    '''
    |p>|x>|y> -> |p>|x>|x+p*y(mod 2**n)> |p> has only 1 qubit
    '''
    c = tc.Circuit(max([p] + x + y) + 1)
    n = len(x)
    c.append(QFT(y))
    for i in range(n):
        for j in range(n - 1 - i, n):
            c.append(ccphase(p, x[i], y[j], theta=np.pi / (2 ** (i + j - n + 1))))
    c.append(QFT(y).inverse())
    return c
