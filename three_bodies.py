import matplotlib.pyplot as plt
import numpy as np
from random import seed
from input import *
import functions as f



seed(seed_n)
n_iter = 10
# all_a = np.linspace(0, b + 0.5, 10)
all_a = [0.1, 0.2, 0.3, 0.38, 0.4, 0.43, 0.5, 0.58 , 0.61, 0.63]
all_a = np.sort(all_a)
    
omegas = np.ones(N) + deltas

for a in all_a:
    pops_all = []
    t_env = 0
    t_total = 0
    print("Starting a = {}".format(a))
    for j in range(n_iter):
        pops, thetas = f.get_ini(3)
        for i in range(i_max):
            pops, thetas = f.rk4(pops, thetas, omegas, t_env, a, b)
            t_env = f.period(t_env + dt)
            t_total = (i + 1) * dt
        pops_all.append(pops)
        if (j + 1) % 5: print("\tProgress {:.2f} %".format((j + 1) / n_iter * 100), end="\r", flush=True)
    print("\tProgress 100.00 %")
    np.array(pops_all)
    avgs = np.sum(pops_all, axis=0) / n_iter
    print("\tAverages are {:.2f}".format(avgs))

fig = plt.figure(figsize=(6.4*1.5, 4.8))
ax = fig.add_subplot(121)

ax.scatter(all_a, pops_all)

plt.show()