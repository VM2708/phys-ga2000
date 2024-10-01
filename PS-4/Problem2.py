#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:37:32 2024

@author: vedhasyamuvva
"""
#Exercise 5.10 pg 183/559
import numpy as np
import matplotlib.pyplot as plt

def f(a,x):
    return 1/(np.sqrt(a**4-x**4))
    
def T(a):
    N = 20
    m = 1
    
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.legendre.leggauss(N)
    
    
    xp = (0.5*(a))*x + 0.5*(a)
    wp = 0.5*(a)*w
    
    s = 0.0
    for k in range(N):
        s+= wp[k] * f(a,xp[k])
        
    return(np.sqrt(8*m)*s)

def Tarr(Aarr):
    Tarr = np.empty(np.size(Aarr))
    for i in range (np.size(Aarr)):
        Tarr[i] = T(Aarr[i])
    return Tarr

STEP_SIZE = 0.1
Aarr = np.arange(STEP_SIZE,2+STEP_SIZE,STEP_SIZE)
plt.plot(Aarr, Tarr(Aarr))
plt.xlabel("Amplitude")
plt.ylabel("Period")
plt.title("Period Of Oscillation for V(X) = x^4")
plt.savefig("periodOfOscillation.png")



