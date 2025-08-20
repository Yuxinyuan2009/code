import tensorcircuit as tc

def set(n, x):
    '''
    设置初态
    '''
    c = tc.Circuit(max(x) + 1)
    l = 0
    while n > 0:
        c.X(x[-l - 1]) if n % 2 == 1 else c.I(x[-l - 1])
        n //= 2
        l += 1
    return c


def out(x):
    for i in range(len(x)):
        if abs(x[i]) > 0.001:
            print(i % 16, end=" ")

# for i in range(16):
#     c = tc.Circuit(4)
#     c = set(i, [0, 1, 2, 3])
#     print(f"{i},{out(c.state())}")

def ccphase(p, x, y, theta):
    c = tc.Circuit(max([p] + [x] + [y]) + 1)
    c.cphase(x, y, theta=theta / 2.)
    c.cnot(p, x)
    c.cphase(x, y, theta=-theta / 2.)
    c.cnot(p, x)
    c.cphase(p, y, theta=theta / 2.)
    return c

