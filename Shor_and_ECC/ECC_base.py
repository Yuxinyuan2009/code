import tensorcircuit as tc
from mod_mul import *
from negation import *
from cmod_square import *

def ECC_add(x1, y1, x2, y2, a, z):
    '''
    Q = (x2, y2)
    |Q> -> |Q + P>
    '''
    c = tc.Circuit(max(x2 + y2 + z) + 1)

    c.append(mod_add_const(x2, [z[0]], (7 - x1) % 7))
    c.append(mod_add_const(y2, [z[0]], (7 - y1) % 7))
    # now: x2 - x1, y2 - y1, 0
    c.multicontrol(*(x2[1:4] + y2[1:4] + [x2[0]]), unitary=tc.gates._x_matrix, ctrl=[0, 0, 0, 0, 0, 0])
    c.append(cmod_add_const(x2[0], z[0:4], [z[4]], (3 * x1 + a) * ((2 * y1)**5) % 7))
    c.multicontrol(*(x2[1:4] + y2[1:4] + [x2[0]]), unitary=tc.gates._x_matrix, ctrl=[0, 0, 0, 0, 0, 0])
    # corner case: P = Q
    c.append(inv(x2))
    c.append(mod_mul(x2, y2, [z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(inv(x2))
    # now: x2 - x1, y2 - y1, lambda
    c.append(mod_add_const(x2, [z[0]], x1 % 7))
    c.append(negation(x2, [z[4]]))
    c.append(mod_mul(x2, [z[0], z[1], z[2], z[3]], y2, [z[4]]))
    c.append(negation(y2, [z[4]]))
    # now: -x2, lambda * x2 - y2 + y1, lambda
    c.append(mod_square([z[0], z[1], z[2], z[3]], x2, [z[4]]))
    c.append(mod_add_const(x2, [z[4]], (7 - x1) % 7))
    # now: x3, lambda * x2 - y2 + y1, lambda
    # = x3, lambda * x1, lambda
    c.append(negation([z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(mod_mul(x2, [z[0], z[1], z[2], z[3]], y2, [z[4]]))
    c.append(mod_add_const(x2, [z[4]], (7 - x1) % 7))
    c.append(negation([z[0], z[1], z[2], z[3]], [z[4]]))
    # now: x3 - x1, lambda * (x1 - x3), lambda
    c.append(inv(x2))
    c.append(mod_mul(x2, y2, [z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(inv(x2))
    # now: x3 - x1, lambda * (x1 - x3), 0
    c.append(mod_add_const(x2, [z[4]], x1 % 7))
    c.append(mod_add_const(y2, [z[4]], (7 - y1) % 7))
    return c
'''
c = tc.Circuit(13)
c.append(set(3, [5, 6, 7, 8]))
c.append(set(3, [9, 10, 11, 12]))
c.append(ECC_add(3, 3, [5, 6, 7, 8], [9, 10, 11, 12], 3, [1, 2, 3, 4, 0]))
out(c.state())
'''

def cond_ECC_add(p, x1, y1, x2, y2, a, z):
    '''
    Q = (x2, y2)
    |Q> -> |Q + P>
    '''
    c = tc.Circuit(max([p] + x2 + y2 + z) + 1)

    c.append(mod_add_const(x2, [z[0]], (7 - x1) % 7))
    c.append(mod_add_const(y2, [z[0]], (7 - y1) % 7))
    # now: x2 - x1, y2 - y1, 0
    c.multicontrol(*([p] + x2[1:4] + y2[1:4] + [x2[0]]), unitary=tc.gates._x_matrix, ctrl=[1, 0, 0, 0, 0, 0, 0])
    c.append(cmod_add_const(x2[0], z[0:4], [z[4]], (3 * x1 + a) * ((2 * y1)**5) % 7))
    c.multicontrol(*([p] + x2[1:4] + y2[1:4] + [x2[0]]), unitary=tc.gates._x_matrix, ctrl=[1, 0, 0, 0, 0, 0, 0])
    # corner case: P = Q
    c.append(inv(x2))
    c.append(mod_mul(x2, y2, [z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(inv(x2))
    # now: x2 - x1, y2 - y1, lambda
    c.append(mod_add_const(x2, [z[0]], x1 % 7))
    c.append(negation(x2, [z[4]]))
    c.append(mod_mul(x2, [z[0], z[1], z[2], z[3]], y2, [z[4]]))
    c.append(negation(y2, [z[4]]))
    # now: -x2, lambda * x2 - y2 + y1, lambda
    c.append(cmod_square(p, [z[0], z[1], z[2], z[3]], x2, [z[4]]))
    c.append(cmod_add_const(p, x2, [z[4]], (7 - x1) % 7))
    # now: x3, lambda * x2 - y2 + y1, lambda
    # = x3, lambda * x1, lambda
    c.append(cnegation(p, [z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(mod_mul(x2, [z[0], z[1], z[2], z[3]], y2, [z[4]]))
    c.x(p)
    c.append(cnegation(p, x2, [z[4]]))
    c.x(p)
    c.append(mod_add_const(x2, [z[4]], (7 - x1) % 7))
    c.append(cnegation(p, [z[0], z[1], z[2], z[3]], [z[4]]))
    # now: x3 - x1, lambda * (x1 - x3), lambda
    c.append(inv(x2))
    c.append(mod_mul(x2, y2, [z[0], z[1], z[2], z[3]], [z[4]]))
    c.append(inv(x2))
    # now: x3 - x1, lambda * (x1 - x3), 0
    c.append(mod_add_const(x2, [z[4]], x1 % 7))
    c.append(mod_add_const(y2, [z[4]], (7 - y1) % 7))
    c.x(p)
    c.append(cnegation(p, y2, [z[4]]))
    c.x(p)
    return c


c = tc.Circuit(14)
c.append(set(3, [6, 7, 8, 9]))
c.append(set(3, [10, 11, 12, 13]))
c.x(5)
c.append(cond_ECC_add(5, 2, 5, [6, 7, 8, 9], [10, 11, 12, 13], 3, [1, 2, 3, 4, 0]))
c.x(5)
out(c.state())
print(c.gate_count())
c.draw(output="mpl").savefig("ECC_add.png")