import tensorcircuit as tc
from add_const import *

def mod_add_const(x, z, t):
    '''
    z[0]:ancilla qubit
    |x> -> |x+t(mod p)>
    '''
    t = t % 7
    c = tc.Circuit(max(x + z) + 1)
    c.append(add_const(x, t + 1))
    c.cnot(x[0], z[0])
    c.append(cadd_const(z[0], x, 9))
    c.append(add_const(x, -(t + 1)))
    c.cnot(x[0], z[0])
    c.append(add_const(x, t))
    return c
'''
for i in range(7):
    for j in range(7):
        c = tc.Circuit(5)
        c.append(set(i, [1, 2, 3, 4]))
        c.append(mod_add_const([1, 2, 3, 4], [0], j))
        print(f"{i} + {j} = ", end="")
        out(c.state())
        print()
'''

def cmod_add_const(p, x, z, t):
    '''
    p:control qubit, z[0]:ancilla qubit
    '''
    t = t % 7
    c = tc.Circuit(max(x + z + [p]) + 1)
    c.append(add_const(x, t + 1))
    c.toffoli(p, x[0], z[0])
    c.append(ccadd_const(p, z[0], x, 9))
    c.append(add_const(x, -(t + 1)))
    c.toffoli(p, x[0], z[0])
    c.append(cadd_const(p, x, t))
    return c
'''
for i in range(7):
    for j in range(7):
        c = tc.Circuit(6)
        c.append(set(i, [2, 3, 4, 5]))
        c.append(cmod_add_const(1, [2, 3, 4, 5], [0], j))
        print(f"{i} + {j} = ", end="")
        out(c.state())
        print()
'''
def ccmod_add_const(p, q, x, z, t):
    t = t % 7
    c = tc.Circuit(max(x + z + [p] + [q]) + 1)
    c.append(cmod_add_const(p, x, z, t * 4 % 7))
    c.cnot(q, p)
    c.append(cmod_add_const(p, x, z, t * 3 % 7))
    c.cnot(q, p)
    c.append(cmod_add_const(q, x, z, t * 4 % 7))
    return c
