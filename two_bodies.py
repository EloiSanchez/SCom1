import matplotlib.pyplot as plt
import numpy as np
from random import seed
from parameters import *
import functions as f

# Initial parameters
seed(seed_n)

pops, thetas = f.get_ini(N)

# Obtain analytical results from paper
alphas = g * f.get_A(np.arcsin(deltas / r))
v = 1 + b * np.cos(0)
phi0 = np.arcsin(deltas[0] / r)
phi1 = np.arcsin(deltas[1] / r)
w = 1 + b * np.cos(phi0 - phi1)
wv = w / v
a2a1 = alphas[1] / alphas[0]
print("TWO BODIES PARAMETERS")
print("delta 1 = {:.3f}, delta 2 = {:.3f}".format(deltas[0], deltas[1]))
print("alpha 1 = {:.3f}, alpha 2 = {:.3f}".format(alphas[0], alphas[1]))
print("w = {:.3f}".format(v))
print("v = {:.3f}".format(w))
print("w/v = {:.3f}".format(wv))
print("alpha 2 / alpha 1 = {:.3f}\n".format(a2a1))
if wv < a2a1:
    print("Both species should survive\n")
elif wv > a2a1:
    print("Only 1 should survive\n")
else:
    print("This is broken\n")
    quit()
ratio = (alphas[0] - alphas[1]) / (v - w)
omegas = np.ones(N) + deltas

# Run numerical dynamics
pops_all, thetas_all, t_all, t_env_all, ratios_all = [], [], [], [], []
t_env = 0
t_total = 0
for i in range(i_max):
    pops, thetas = f.rk4(pops, thetas, omegas, t_env, a, b)
    t_env = f.period(t_env + dt)
    t_total = (i + 1) * dt
    pops_all.append(pops)
    thetas_all.append([f.subtract_ang(x) for x in np.abs(thetas - t_env)])
    t_env_all.append(t_env)
    t_all.append(t_total)
    ratios_all.append(pops[0] - pops[1])

pops_all, thetas_all, ratios_all = [np.array(x) for x in (pops_all, thetas_all, ratios_all)]

# Plot results and compare with analytical
fig = plt.figure(figsize=(6.4*2, 4.8))
ax_pops = fig.add_subplot(131)
ax_thetas = fig.add_subplot(132)
ax_ratios = fig.add_subplot(133)

ax_thetas.plot(t_all, t_env_all, label="Env", c="green")

for i in range(N):
    ax_pops.plot(t_all, pops_all[:, i], label="{}".format(i))
    ax_thetas.plot(t_all, thetas_all[:, i], label="theta {}".format(i))

ax_ratios.plot(t_all, ratios_all)
ax_ratios.hlines(ratio, 0, np.max(t_all), colors="black", linestyles="dashed")

ax_pops.legend()
ax_thetas.legend()
ax_ratios.legend()
plt.show()
