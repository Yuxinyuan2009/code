import tensorcircuit as tc
from mod_add import *

def doubling(x, z):
    '''
    |x> -> |2x(mod p)>
    z[0]: ancilla qubit
    '''
    c = tc.Circuit(max(x + z) + 1)
    for i in range(3):
        c.swap(x[i], x[i + 1])
    # |x> -> |2x>
    c.cnot(x[0], z[0])
    c.append(cadd_const(z[0], x, 9))
    c.cnot(x[3], z[0])
    return c
'''
for i in range(7):
    c = tc.Circuit(5)
    c.append(set(i, [1, 2, 3, 4]))
    c.append(doubling([1, 2, 3, 4], [0]))
    out(c.state())
'''