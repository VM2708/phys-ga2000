#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:45:31 2024

@author: vedhasyamuvva
"""

#pg 359, Exercise 8.6
import numpy as np
import matplotlib.pyplot as plt

w = 1
mu = 4 #and 1, 2, 4
ANHARMONIC = False

def f(r,t):
    x = r[0]
    v = r[1]
    fx = v
    if ANHARMONIC == False: fv = -w**2 * x + mu*(1-x**2)*v
    if ANHARMONIC == True:  fv = -w**2*x**3 #FOR anharmonic
    return np.array([fx, fv], float)

a = 0.0
b = 50
N = 1000
h = (b-a)/N
tpoints = np.arange(a,b,h)
xpoints = np.zeros_like(tpoints)
vpoints = np.zeros_like(tpoints)

x_initial = 1 #1 or 2
v_initial = 0
r = np.array([x_initial,v_initial])
for i in range (np.size(tpoints)):
    xpoints[i] = r[0]
    vpoints[i] = r[1]
    t = tpoints[i]
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t + 0.5*h)
    k3 = h*f(r+0.5*k2, t + 0.5*h)
    k4 = h*f(r+k3, t + h)
    r = r + (k1+2*k2+2*k3+k4)/6

if (mu == 0):
    plt.xlabel("Time (s)")
    plt.ylabel("Distance From Equilibrium (units)")
    if ANHARMONIC == True: plt.title("Anharmonic Oscillator")
    if ANHARMONIC == False: plt.title("Harmonic Oscillator")
    plt.plot(tpoints, xpoints)
    if ANHARMONIC == False: plt.savefig(f"x0_{x_initial}.png")
    if ANHARMONIC == True:  plt.savefig(f"anharmonic_x0_{x_initial}.png")
    plt.show()
else:
    plt.plot(xpoints, vpoints)
    
    plt.xlabel("Distance From Equilibrium (units)")
    plt.ylabel("Velocity (units/sec)")
    plt.title("van der Pol Oscillators")
    
    plt.savefig(f"van_mu_{mu}")
    plt.show()