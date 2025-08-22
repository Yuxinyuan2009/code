import tensorcircuit as tc
from mod_add_const import *

def cccmod_add_const(p, q, r, x, z, t):
    t = t % 7
    c = tc.Circuit(max([p, q, r] + x + z) + 1)
    c.append(ccmod_add_const(p, r, x, z, t * 4 % 7))
    c.cnot(q, p)
    c.append(ccmod_add_const(p, r, x, z, t * 3 % 7))
    c.cnot(q, p)
    c.append(ccmod_add_const(q, r, x, z, t * 4 % 7))
    return c

def cmod_square(p, x, y, z):
    '''
    p:control qubit, z[0]:ancilla qubit
    |x>|y> -> |x>|y+x^2(mod p)>
    '''
    c = tc.Circuit(max([p] + x + y + z) + 1)
    for i in range(1, 4):
        for j in range(i, 4):
            if i == j:
                c.append(ccmod_add_const(p, x[i], y, z, 2**(6 - i - j) % 7))
            else:
                c.append(cccmod_add_const(p, x[i], x[j], y, z, 2**(7 - i - j) % 7))
    return c
