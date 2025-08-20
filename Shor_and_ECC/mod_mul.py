import tensorcircuit as tc
from mod_add import *
from doubling import *
from mod_add_const import *

def mod_mul(x, y, z, anc):
    '''
    |x>|y>|z>  ->|x>|y>|z+x*y(mod p)>
    '''
    c = tc.Circuit(max(x + y + z + anc) + 1)
    for i in range(3):
        c.append(cmod_add(x[3 - i], y, z, anc))
        c.append(doubling(y, anc))
    return c
'''
for i in range(7):
    for j in range(7):
        c = tc.Circuit(13)
        c.append(set(i, [1, 2, 3, 4]))
        c.append(set(j, [5, 6, 7, 8]))
        c.append(mod_mul([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0]))
        print(f"{i} * {j} = ", end="")
        out(c.state())
        print()

c = tc.Circuit(13)
c.append(mod_mul([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0]))
out(c.state())
print(c.gate_count())
c.draw(output="mpl").savefig("mod_mul.png")
# 1074 gates
'''

def mod_square(x, y, z):
    '''
    z[0]:ancilla qubit
    |x>|y> -> |x>|y+x^2(mod p)>
    '''
    c = tc.Circuit(max(x + y + z) + 1)
    for i in range(1, 4):
        for j in range(i, 4):
            if i == j:
                c.append(cmod_add_const(x[i], y, z, 2**(6 - i - j) % 7))
            else:
                c.append(ccmod_add_const(x[i], x[j], y, z, 2**(7 - i - j) % 7))
    return c

'''
for i in range(7):
    for j in range(7):
        c = tc.Circuit(9)
        c.append(set(i, [1, 2, 3, 4]))
        c.append(set(j, [5, 6, 7, 8]))
        c.append(mod_square([1, 2, 3, 4], [5, 6, 7, 8], [0]))
        print(f"{j} + {i} * {i} = ", end="")
        out(c.state())
        print()

c = tc.Circuit(9)
c.append(mod_square([1, 2, 3, 4], [5, 6, 7, 8], [0]))
c.draw(output="mpl").savefig("mod_square.png")
print(c.gate_count())
# 1666 gates
'''

def inv(x):
    c = tc.Circuit(max(x) + 1)
    c.swap(x[1], x[2])
    return c

