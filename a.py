import tensorcircuit as tc
import numpy as np

c = tc.Circuit(1)
c.H(0)
readout_error = [[0.9, 0.75],[0.4, 0.7]]
print(c.sample_expectation_ps(x=[0]))