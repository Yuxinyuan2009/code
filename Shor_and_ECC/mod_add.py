import tensorcircuit as tc
import numpy as np
from add_const import *
import matplotlib
def mod_add(x, y, z):
    c = tc.Circuit(max(x + y + z) + 2)
    c.append(add(x, y))
    c.append(add_const(y, 9))
    c.cnot(y[0], z[0])
    c.append(cadd_const(z[0], y, 7))
    c.append(add(x, y).inverse())
    c.x(y[0])
    c.cnot(y[0], z[0])
    c.x(y[0])
    c.append(add(x, y))
    return c
'''
for i in range(7):
    for j in range(7):
        c = tc.Circuit(9)
        c.append(set(i, [0, 1, 2, 3]))
        c.append(set(j, [4, 5, 6, 7]))
        c.append(mod_add(list(range(4)), list(range(4, 8)), [8]))
        print(f"{i} + {j} = ", end="")
        out(c.state())
        print()

c = tc.Circuit(9)
c.append(mod_add(list(range(4)), list(range(4, 8)), [8]))
c.draw(output="mpl").savefig("mod_add.png")
'''
def cmod_add(p, x, y, z):
    '''
    p: control qubit z[0]: ancilla qubit
    '''
    c = tc.Circuit(max(x + y + z + [p]) + 2)
    c.append(cadd(p, x, y))
    c.append(add_const(y, 9))
    c.toffoli(p, y[0], z[0])
    c.append(ccadd_const(p, z[0], y, 7))
    c.append(cadd(p, x, y).inverse())
    c.x(y[0])
    c.toffoli(p, y[0], z[0])
    c.x(y[0])
    c.append(cadd(p, x, y))
    return c
'''
c = tc.Circuit(10)
c.x(1)
c.append(set(6, [2, 3, 4, 5]))
c.append(set(5, [6, 7, 8, 9]))
c.append(cmod_add(1, [2, 3, 4, 5], [6, 7, 8, 9], [0]))
out(c.state())
'''