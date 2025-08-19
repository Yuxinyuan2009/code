import tensorcircuit as tc
from mod_add import *

def negation(x, z):
    '''
    |x> -> |-x(mod p)>
    z[0]: ancilla qubit
    '''
    c = tc.Circuit(max(x + z) + 1)
    c.x(x[0])
    c.x(x[1])
    c.x(x[2])
    c.x(x[3])
    c.append(add_const(x, 9))
    c.cnot(x[0], z[0])
    c.append(cadd_const(z[0], x, 9))
    c.append(add_const(x, 14))
    c.cnot(x[0], z[0])
    c.append(add_const(x, 1))
    return c
'''
for i in range(7):
    c = tc.Circuit(5)
    c.append(set(i, [1, 2, 3, 4]))
    c.append(negation([1, 2, 3, 4], [0]))
    out(c.state())
'''
def cnegation(p, x, z):
    '''
    p:control qubit, z[0]:ancilla qubit
    '''
    c = tc.Circuit(max(x + z + [p]) + 1)
    c.cnot(p, x[0])
    c.cnot(p, x[1])
    c.cnot(p, x[2])
    c.cnot(p, x[3])
    c.append(cadd_const(p, x, 9))
    c.cnot(x[0], z[0])
    c.append(ccadd_const(p, z[0], x, 9))
    c.append(cadd_const(p, x, 14))
    c.toffoli(p, x[0], z[0])
    c.append(cadd_const(p, x, 1))
    return c
'''
for i in range(7):
    c = tc.Circuit(6)
    c.append(set(i, [2, 3, 4, 5]))
    c.x(1)
    c.append(cnegation(1, [2, 3, 4, 5], [0]))
    out(c.state())
'''