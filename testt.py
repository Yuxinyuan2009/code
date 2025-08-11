import tensorcircuit as tc
import numpy as np

c = tc.Circuit(2)
c.H(0)
readout_error = []
readout_error.append([0.9,0.75])
readout_error.append([0.4,0.7])
print(c.sample_expectation_ps(x=[0], y=[1],readout_error = readout_error))