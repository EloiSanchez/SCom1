import numpy as np

N = 2  # Nº of species

deltas = np.array(
    [0.27, -0.3]  # Phase shifts for N = 2, 3, ...
    # [-0.27, 0, 0.27]
  )

r = 0.333  # Environment parameter
g = 1    # Growth parameter
a = 1  # Growth amplitude
b = 0.6  # Competition amplitude

dt = 0.01
i_max = 10000
seed_n = 12345

results_dir = "two_bodies"

# Two bodies conditions
# Keep everything fixed and change delta 1
# For 0.4 < delta 1 < 0.0631 only one survives
# For 0.0631 < delta 1 < 0.4 both survive
# N = 2  # Nº of species

# deltas = np.array(
#     [0.05, -0.4]  # Phase shifts for N = 2, 3, ...
#   )

# r = 0.7  # Environment parameter
# g = 1    # Growth parameter
# a = 1  # Growth amplitude
# b = 0.6  # Competition amplitude

# dt = 0.01
# i_max = 10000
# seed_n = 12345
