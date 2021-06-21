import matplotlib.pyplot as plt
import numpy as np
from random import seed
from input import *
import functions as f
from shutil import copy

results_dir = f.make_dir(results_dir)

seed(seed_n)
n_iter = 1
# all_a = np.linspace(0, b + 0.5, 10)
all_a = np.array(
    [0, 0.1, 0.2, 0.3, 0.38, 0.4, 0.43, 0.5, 0.58 , 0.63, 0.7]
)
# all_a = np.sort(all_a)

omegas = np.ones(N) + deltas
avgs_all = []

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
    print("\tAverages are {}".format(avgs))
    avgs_all.append(avgs)

avgs_all = np.array(avgs_all)

fig = plt.figure(figsize=(6.4*1.5, 4.8))
ax = fig.add_subplot()

for i in range(N):
    ax.scatter(all_a, avgs_all[:,i], label=r"$x_{}$".format(i+1))

ax.legend()
# plt.show()
fig.savefig(results_dir + "/populations.png")

copy("input.py", results_dir + "/")

file_avgs = open(results_dir + "/averages.txt", mode="w")
file_avgs.write("# Averages over {}\n".format(n_iter))
for i in range(len(all_a)):
    file_avgs.write("{} {}\n".format(all_a[i], *avgs_all[i,:]))
