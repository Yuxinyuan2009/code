import tensorcircuit as tc
import numpy as np

c = tc.Circuit(2)
c.cphase(0, 1, theta=np.pi)
print(c.matrix())