import numpy as np
from random import random
from parameters import *

def get_ini(n):
    return np.array([random() for i in range(n)]), np.array([random() * np.pi * 2 for i in range(n)])

def get_A(a, t):
    return 1 - a * np.cos(np.abs(a - t))

def get_B(thetas):
    angs1 = np.broadcast_to(thetas, (N,N))
    return 1 - np.cos(np.abs(angs1 - np.transpose(angs1)))

def func_pop(pops, thetas, t, i):
    res = pops[i] * g * get_A(thetas[i], t)
    res -= np.dot(get_B(thetas), pops)
    return res * pops[i]

def func_theta(thetas, omegas, t):
    return omegas - r * np.sin(thetas - t)

def rk4(pops, thetas, t):
    pops_old = pops.copy()
    thetas_old = thetas.copy()
    

def period(t):
    if t >= np.pi:
        t -= 2 * np.pi
    return t
