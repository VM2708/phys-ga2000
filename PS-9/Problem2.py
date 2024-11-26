#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:05:38 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

MASS = 1
RADIUS = 0.08
theta_i = 30 #deg
VELOCITY_i = 100
RHO = 1.22
C = 0.47
g = 9.81

vx_initial =  VELOCITY_i * np.cos(theta_i*np.pi/180)
vy_initial = VELOCITY_i * np.sin(theta_i*np.pi/180)
x_initial = 0
y_initial = 0


def f(r,t,M):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    
    fx = vx
    fvx = -np.pi*RADIUS**2*RHO*C/(2*M) * vx * (vx**2+vy**2)**(1/2)
    fy = vy
    fvy = -np.pi*RADIUS**2*RHO*C/(2*M)* vy *(vx**2+vy**2)**(1/2) - g
    return np.array([fx, fy, fvx, fvy], float)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N
tpoints = np.arange(a,b,h)
xpoints = np.zeros_like(tpoints)
ypoints = np. zeros_like(tpoints)
vxpoints = np. zeros_like(tpoints)
vypoints = np. zeros_like(tpoints)

r = np.array([x_initial,y_initial, vx_initial, vy_initial])
def func(r,M):
    for i in range (np.size(tpoints)):
        xpoints[i] = r[0]
        ypoints[i] = r[1]
        vxpoints[i] = r[2]
        vypoints[i] = r[3]
        
        t = tpoints[i]
        k1 = h*f(r,t,M)
        k2 = h*f(r+0.5*k1, t + 0.5*h, M)
        k3 = h*f(r+0.5*k2, t + 0.5*h, M)
        k4 = h*f(r+k3, t + h, M)
        r = r + (k1+2*k2+2*k3+k4)/6
    
        if (tpoints[i] != 0 and ypoints[i] <= 0): 
            xpoints[i+1:]=r[0]
            break

    plt.plot(xpoints,ypoints, label = f"Mass = {M} kg")

PARTC = True #Toggle as needed
func(r,M = MASS)
if PARTC: func(r,M = 2)
if PARTC: func(r,M = 3)
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Projectile Motion of Canonball")
if PARTC: plt.legend()
if not PARTC: plt.savefig("mass1.png")
if PARTC: plt.savefig("massall.png")
plt.show()