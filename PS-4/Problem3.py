#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:53:31 2024

@author: vedhasyamuvva
"""

#Exercise 5.13 pg 192/559
import numpy as np
import math
import matplotlib.pyplot as plt

def H(n, x):
    if n == 0:
        return 1
    if n == 1:
        return 2 * x

    H_nm2 = 1
    H_nm1 = 2 * x

    for i in range(2, n + 1):
        H_n = 2 * x * H_nm1 - 2 * (i - 1) * H_nm2
        H_nm2, H_nm1 = H_nm1, H_n

    return H_n

def wavefunction(n,x):
    return 1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)*H(n,x)

def createWaveFunctionGraph(xarr,narr):
    waveArr = np.empty_like(xarr)
    
    for j in range (np.size(narr)):
        for i in range(np.size(xarr)):
            waveArr[i] = wavefunction(narr[j],xarr[i])
        plt.plot(xarr,waveArr, label = f"n = {narr[j]}")
    plt.xlabel("x")
    plt.ylabel("Wave Function")
    plt.title("Wave function For Various Energy Levels")
    plt.legend()
    plt.savefig("WaveFunctionForMultipleN.png")
    plt.show()

def createSingleWaveFunctionsGraph():
    n = 30
    xarr = np.arange(-10,10,0.1)
    waveArr = np.empty_like(xarr)
    
    for i in range(np.size(xarr)):
        waveArr[i] = wavefunction(n,xarr[i])
    plt.plot(xarr,waveArr, label = "N = 30")
    plt.xlabel("x")
    plt.ylabel("Wave Function")
    plt.title("Wave function For N = 30")
    plt.savefig("WaveFunctionForN30.png")
    plt.show()
    
def f(z,n):
    return (1+z**2)/((1-z**2)**2)*(z/(1-z**2))**2*wavefunction(n,(z/(1-z**2)))**2

def uncertainty(n):
    N = 100
    
    a = -1
    b = 1
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.legendre.leggauss(N)
    
    
    xp = (0.5*(b-a))*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    s = 0.0
    for k in range(N):
        s+= wp[k] * f(xp[k], n)
        
    uncertainty = np.sqrt(11/2) - np.sqrt(s)
    return uncertainty



xarr = np.arange(-4,4.1,0.1)
narr = np.arange(0,5,1)    

createWaveFunctionGraph(xarr, narr)
createSingleWaveFunctionsGraph()

print("uncertainty using Gaussian quadrature ", uncertainty(5))
