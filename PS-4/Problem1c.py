#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:38:24 2024

@author: vedhasyamuvva
"""

#Heat Capacity of a solid (pg 172) part C

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**4*np.exp(x)/(np.exp(x)-1)**2)

def cv(T,N):
    
    V = 1000*10**(-2*3)
    rho = 6.022*10**(28)
    td = 428
    kb = 1.380649 * 10**(-23)
    
    a = 0
    b = td/T
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.legendre.leggauss(N)
    
    
    xp = (0.5*(b-a))*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        s+= wp[k] * f(xp[k])
        
    return(9*V*rho*kb*(T/td)**3*s)

def createArray(T,Narr):
    arr = np.empty(np.size(Narr))
        
    for i in range (np.size(Narr)):
        arr[i] = cv(T,Narr[i])
    return arr

T = 5
Narr = np.arange(10,80,10)
   
plt.plot(Narr,createArray(T,Narr))
plt.xlabel("N")
plt.ylabel("Heat Capacity (J/K)")
plt.title("Heat Capcity of Aluminum As A Function of Temperature")
plt.legend()

plt.savefig("HeatCapacityWithConvergence.png")

