import numpy as np

N = 2  # Nº of species

deltas = np.array(
    [0.27, -0.3]    # Phase shifts for N = 2
    # [-0.27, 0, 0.27]  # Phase shifts for N = 3
  )                   # Ignored otherwise

r = 0.333  # Environment parameter
g = 1    # Growth parameter
a = 1  # Growth amplitude
b = 0.6  # Competition amplitude

dt = 0.01
i_max = 10000
print_every = 10
seed_n = 12345

results_dir = "two_species"

