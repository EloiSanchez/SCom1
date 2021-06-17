import matplotlib.pyplot as plt
import numpy as np
from random import seed
from population import population
from parameters import *
import functions as f

seed(seed_n)

pops, thetas = f.get_ini(N)
omegas = np.ones(N) + deltas

print(thetas)
print(f.func_pop(pops, thetas, 1, 1))