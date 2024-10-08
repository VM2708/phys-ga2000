#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:25:01 2024

@author: vedhasyamuvva
"""

#Heat Capacity of a solid (pg 172)

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**4*np.exp(x)/(np.exp(x)-1)**2)

def cv(T):
    
    V = 1000*10**(-2*3) #m^3
    rho = 6.022*10**(28) #m^-3
    td = 428 # K
    kb = 1.380649 * 10**(-23) #J/K
    
    a = 0
    b = td/T
    
    N = 50
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.legendre.leggauss(N)
    
    
    xp = (0.5*(b-a))*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        s+= wp[k] * f(xp[k])
        
    return(9*V*rho*kb*(T/td)**3*s)

def createArray(Tarr):
    arr = np.empty(np.size(Tarr))
        
    for i in range (np.size(Tarr)):
        arr[i] = cv(Tarr[i])
    return arr

Tarr = np.arange(5,500,1)

plt.plot(Tarr,createArray(Tarr))
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity (J/K) ")
plt.title("Heat Capcity of Aluminum As A Function of Temperature")

plt.savefig("HeatCapacity.png")

