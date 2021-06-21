import matplotlib.pyplot as plt
import numpy as np
from random import seed
from input import *
import functions as f
from shutil import copy

results_dir = f.make_dir(results_dir)

seed(seed_n)
n_iter = 10
all_a = np.array(
    [0, 0.1, 0.2, 0.3, 0.38, 0.4, 0.43, 0.5, 0.58 , 0.63, 0.7]
)
omegas = np.ones(N) + deltas

# Run all dynamics
avgs_all = []
for a in all_a:
    pops_all = []
    t_env = 0
    t_total = 0
    print("\nStarting a = {}".format(a))
    for j in range(n_iter):
        pops, thetas = f.get_ini(3)
        for i in range(i_max):
            pops, thetas = f.rk4(pops, thetas, omegas, t_env, a, b)
            t_env = f.period(t_env + dt)
            t_total = (i + 1) * dt
            if (j + 1) % 100:
                print("\tIter {}. Progress {:.2f} %".format(j+1,i / i_max * 100),\
                    end="\r", flush=True)
        pops_all.append(pops)
    print("\tIter {}.Progress 100.00 %".format(j+1))
    np.array(pops_all)
    avgs = np.sum(pops_all, axis=0) / n_iter
    print("\tAverages are {}".format(avgs))
    avgs_all.append(avgs)

avgs_all = np.array(avgs_all)

# Plots and results

fig = plt.figure(figsize=(6.4, 4.8))
ax = fig.add_subplot()

for i in range(N):
    ax.scatter(all_a, avgs_all[:,i], label=r"$x_{}$".format(i+1))

ax.set_xlabel(r"$a$")
ax.set_title(r"Populations after phase adaptation with different $a$")

ax.legend()
# plt.show()
fig.savefig(results_dir + "/populations.png")

copy("input.py", results_dir + "/")

file_avgs = open(results_dir + "/averages.txt", mode="w")
file_avgs.write("# Averages over {}\n".format(n_iter))
for i in range(len(all_a)):
    file_avgs.write("{} {}\n".format(all_a[i], *avgs_all[i,:]))
