import matplotlib.pyplot as plt
import numpy as np
from random import seed
from parameters import *
import functions as f

seed(seed_n)

pops, thetas = f.get_ini(N)

if N == 2:
    alphas, v, w = f.get_two_param()

omegas = np.ones(N) + deltas

pops_all, thetas_all, t_all, t_env_all = [], [], [], []
t_env = 0
t_total = 0

for i in range(i_max):
    pops, thetas = f.rk4(pops, thetas, omegas, t_env)
    t_env = f.period(t_env + dt)
    t_total = (i + 1) * dt
    pops_all.append(pops)
    thetas_all.append([f.subtract_ang(x) for x in np.abs(thetas - t_env)])
    t_env_all.append(t_env)
    t_all.append(t_total)
    if (i + 1) % 1000 == 0:
        print(i+1, pops[0] - pops[1], (alphas[0] - alphas[1]) / (v - w))

pops_all = np.array(pops_all)
thetas_all = np.array(thetas_all)

fig = plt.figure(figsize=(6.4*1.5, 4.8))
ax_pops = fig.add_subplot(121)
ax_thetas = fig.add_subplot(122)

ax_thetas.plot(t_all, t_env_all, label="Env", c="green")

for i in range(N):
    ax_pops.plot(t_all, pops_all[:, i], label="{}".format(i))
    ax_thetas.plot(t_all, thetas_all[:, i], label="theta {}".format(i))

ax_pops.legend()
ax_thetas.legend()
plt.show()