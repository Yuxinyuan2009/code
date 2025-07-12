import tensorcircuit as tc
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la
import math

K = tc.set_backend("tensorflow")

c = tc.Circuit(2)
c.h(0)
c.cx(0, 1)
print(c.state())
print(c.expectation_ps(z=[0, 1]))
