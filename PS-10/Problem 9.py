#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:41:21 2024

@author: vedhasyamuvva
"""

import numpy as np
import dcst
import matplotlib.pyplot as plt
import matplotlib.animation as animation


m = 9.109*1e-31
L = 1e-8
x0 = L/2
sigma = 1e-10
kappa = 5e10
N = 1000 #Should be 1000
a = L/N
h = 1e-18
hbar = 6.62607015 * 1e-34
T = 5 # how many time steps


xarr = np.arange(0,L,a)

#Define phi(x,t) = phi[x] which is rewritten for each timestep and define intiial conditions
phi = np.exp(-(xarr-x0)**2 / (2*sigma**2)) * np.exp(1j*kappa*(xarr))

phi_real = phi.real
phi_im = phi.imag

alpha = dcst.dst(phi.real)
eta = dcst.dst(phi.imag)

c = np.empty(N)
def phiAtTime(t):
    
    for i in range (N):
        inside = np.pi**2 * hbar * i**2 / (2* m * L**2) * t
        c[i] = alpha[i]*np.cos(inside) + eta[i] * np.sin(inside)
    
    phi = dcst.idst(c)
    return phi

t = 0

def nextphi(phi):
    global t
    t += 1e-18
    phi = phiAtTime(t)
    return phi

def update(frame):
    global phi
    phi = nextphi(phi)
    
    line.set_ydata(phi.real)
    return line,


fig, ax = plt.subplots()
line, = ax.plot(xarr, phi) 
ax.set_title("Particle in a Box: Spectral Method")
ax.set_xlabel("Position (m)")
ax.set_ylabel("psi (m^(-1/2))")
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)

ani = animation.FuncAnimation(fig, update, frames=T, interval=100, blit=False)

plt.show()
