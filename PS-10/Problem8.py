#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:24:52 2024

@author: vedhasyamuvva
"""
import numpy as np
import banded
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


a1 = 1 + h * (1j*hbar)/(2*m*a**2)
a2 = -h * (1j*hbar)/(4*m*a**2)
b1 = 1 - h * (1j*hbar)/(2*m*a**2)
b2=   h * (1j*hbar)/(4*m*a**2)

A = np.zeros((3,N), dtype = complex)
A[1, :] = a1  # Main diagonal
A[0, 1:] = a2  # Superdiagonal
A[2, :-1] = a2  # Subdiagonal 
              

xarr = np.arange(0,L,a)

#Define phi(x,t) = phi[x] which is rewritten for each timestep and define intiial conditions
phi = np.exp(-(xarr-x0)**2 / (2*sigma**2)) * np.exp(1j*kappa*(xarr))

def nextphi(phi):
    v = np.zeros_like(phi)
    
    for i in range (N):
        if i == 0: 
            v[i] = b1*phi[i] + b2 * (phi[i+1] + 0)
        elif i >= N-1:
            v[i] = b1*phi[i] + b2 * (0 + phi[i-1])
        else:
            v[i] = b1*phi[i] + b2 * (phi[i+1] + phi[i-1])
    phi = banded.banded(A,v,1,1)
    return phi

def update(frame):
    global phi
    phi = nextphi(phi)
    
    line.set_ydata(phi.real)
    return line,


fig, ax = plt.subplots()
line, = ax.plot(xarr, phi.real) 
ax.set_title("Particle in a Box: Crank Nicolson Method ")
ax.set_xlabel("Position (m)")
ax.set_ylabel("psi (m^(-1/2))")
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)

ani = animation.FuncAnimation(fig, update, frames=T, interval=100, blit=False)

plt.show()


