import numpy as np
from random import random
from input import N, dt, g, r, i_max
import os

def make_dir(dir):
    # Check if there are any problems for directory results and create it
    if os.path.exists(dir):
        dirControl = True
        while dirControl:
            choice = input("""
The directory {} already exists. I want to... 
    ...rename the results directory (R)
    ...overwrite the existing directory (O)
    ...exit program (X)
>> """.format(dir)).lower().strip()
            if choice.startswith('r'):
                dir = input('\nIntroduce new directory >> ')
                os.makedirs(dir)
                dirControl = False
            elif choice.startswith('o'):
                print('\nOverwriting existing directory.')
                dirControl = False
            elif choice.startswith('x'):
                print('\nEnd Program\n')
                quit()
    else:
        os.makedirs(dir)
    return dir
    
def get_ini(n):
    return np.array([random() for i in range(n)]), np.array([random() * np.pi * 2 for i in range(n)])

def get_A(thetas, t = 0, a = 1):
    return 1 + a * np.cos(np.array([subtract_ang(x, t) for x in thetas]))

def get_B(thetas, b = 1):
    angs1 = np.broadcast_to(thetas, (N,N))
    return 1 + b * np.cos(subtract_ang(angs1, np.transpose(angs1)))

def func_pop(pops, thetas, t, a, b):
    res = g * get_A(thetas, t, a)
    res -= np.dot(get_B(thetas, b), pops)
    return res * pops

def func_theta(thetas, omegas, t):
    return omegas - r * np.sin(thetas - t)

def rk4(pops, thetas, omegas, t, a, b):
    pops_old = pops.copy()
    thetas_old = thetas.copy()
    kt1 = func_theta(thetas_old, omegas, t)
    kt2 = func_theta(thetas_old + 0.5 * kt1 * dt, omegas, t)
    kt3 = func_theta(thetas_old + 0.5 * kt2 * dt, omegas, t)
    kt4 = func_theta(thetas_old + kt3 * dt, omegas, t)

    kp1 = func_pop(pops_old, thetas_old, t, a, b)
    kp2 = func_pop(pops_old + 0.5 * kp1 * dt, thetas_old + 0.5 * kt1 * dt, t, a, b)
    kp3 = func_pop(pops_old + 0.5 * kp2 * dt, thetas_old + 0.5 * kt2 * dt, t, a, b)
    kp4 = func_pop(pops_old + kp3 * dt, thetas_old + kt3 * dt, t, a, b)

    thetas = thetas_old + dt * (kt1 + kt4 + 2 * (kt2 + kt3)) / 6
    return pops_old + dt * (kp1 + kp4 + 2 * (kp2 + kp3)) / 6, \
           np.array([period(theta) for theta in thetas])

def period(t, thresh = np.pi * 2, remove = np.pi * 2):
    if t >= thresh:
        t -= remove
    return t

def subtract_ang(a1, a2 = 0.):
    """Substracts two angles defined in [0,2pi]. If only a1 is given it is taken
    as the difference. If a1 and a2 are given, the difference is a1 - a2.

    Args:
        a1 (float or np.ndarray): The first angle or difference of angles
        a2 (float, optional): The second angle. Defaults to 0.

    Returns:
        float or np.ndarray: The difference of the angles with periodic conditions applied
    """
    x = np.abs(a1 - a2)
    if type(x) == np.ndarray:
        x = np.where(x > np.pi, 2 * np.pi - x, x)
    elif x > np.pi:
        x = 2 * np.pi - x
    return x

def progress(i):
    print("Progress {:.2f} %".format(i/i_max*100), end="\r", flush=True)