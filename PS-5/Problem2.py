#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:51:31 2024

@author: vedhasyamuvva
"""
#Exercise 5.17

import numpy as np
import matplotlib.pyplot as plt

def f(x,a):
    return np.exp((a-1)*np.log(x) - x)
    #SHOULD USE GAUSS LAGUERRE QUADRATURE
def plotf(xarr,arr):
    yarr = np.empty_like(xarr)
    for a in arr:
        for i in range(np.size(xarr)):
            yarr[i] = f(xarr[i],a)
        plt.plot(xarr,yarr, label = f"a = {a}")
    plt.xlabel("x")
    plt.ylabel("Integrand")
    plt.title("Integrand as a function of x")
    plt.savefig("Problem2a.png")
    
def z(x, a):
    #dz = (a-1)/((a-1)+x)**2 dx
    return x/(a-1+x)

def newIntegrand(z, a):
    x = (a - 1) * z / (1 - z)  # Back-substitute to find x from z
    jacobian = (a - 1) / (1 - z)**2  # The derivative dx/dz
    return f(x, a) * jacobian

xarr = np.arange(0,5,0.1)
arr = np.arange(2,5,1)

plotf(xarr,arr)


def gamma(a):
    
    low = 0
    high = 1
    
    N = 100
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.legendre.leggauss(N)
    
    
    xp = (0.5*(high-low))*x + 0.5*(high+low)
    wp = 0.5*(high-low)*w
    
    s = 0.0
    for k in range(N):
        s+= wp[k] * newIntegrand(xp[k],a)
    return(s)

print("gamma of 3/2: ", gamma(3/2))
print("error: ", np.sqrt(np.pi)/2 - gamma(3/2))
print("gamma of 3: ", gamma(3))
print("gamma of 6: ", gamma(6))
print("gamma of 10: ", gamma(10))