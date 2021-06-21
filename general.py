import matplotlib.pyplot as plt
import numpy as np
from random import seed
from input import *
import functions as f
from shutil import copy
from random import random

results_dir = f.make_dir(results_dir)

# Initial parameters
seed(seed_n)

pops, thetas = f.get_ini(N)
omegas = np.linspace(1 - r * 0.9, 1 + r * 0.9, N)

# Run numerical dynamics
pops_all, thetas_all, t_all, t_env_all = [], [], [], []
t_env = 0
t_total = 0
for i in range(i_max):
    if (i+1) % 100 == 0: f.progress(i)
    pops, thetas = f.rk4(pops, thetas, omegas, t_env, a, b)
    t_env = f.period(t_env + dt)
    t_total = (i + 1) * dt
    pops_all.append(pops)
    thetas_all.append([f.subtract_ang(x) for x in np.abs(thetas - t_env)])
    t_env_all.append(t_env)
    t_all.append(t_total)

pops_all, thetas_all = [np.array(x) for x in (pops_all, thetas_all)]

# Plots and results

fig = plt.figure(figsize=(6.4*2, 4.8))
ax_pops = fig.add_subplot(121)
ax_thetas = fig.add_subplot(122)

for i in range(N):
    ax_pops.plot(t_all, pops_all[:, i], label=r"$x_{}$".format(i+1))
    ax_thetas.plot(t_all, thetas_all[:, i], label=r"$\theta_{}-t$".format(i+1))

ax_pops.set_title("Population evolution")
ax_pops.set_xlabel("Time (A.U.)")
ax_pops.legend(ncol=1, fontsize='small', bbox_to_anchor=(-0.1,1))

ax_thetas.set_title("Phase difference evolution")
ax_thetas.set_xlabel("Time (A.U.)")
ax_thetas.legend(ncol=1, fontsize='small', bbox_to_anchor=(1.2,1))

# plt.show()
fig.savefig(results_dir + "/plot.png")

copy("input.py", results_dir + "/")

file_pop = open(results_dir + "/populations.txt", mode="w")
file_thetas = open(results_dir + "/thetas.txt", mode="w")
for i in range(i_max):
    file_pop.write("{} {}\n".format(t_all[i], " ".join(map(str, pops_all[i,:]))))
    file_thetas.write("{} {}\n".format(t_all[i], " ".join(map(str, thetas_all[i,:]))))    
[f.close() for f in (file_pop, file_thetas)]
file_omegas = open(results_dir + "/omegas.txt", mode="w")
for i in range(N):
    file_omegas.write("species {} -> omega {}".format(i+1, omegas[i]))
file_omegas.close()