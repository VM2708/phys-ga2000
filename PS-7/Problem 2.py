#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:40:08 2024

@author: vedhasyamuvva
"""

import numpy as np
import scipy

def f(x):
    return (x-0.3)**2*np.exp(x)

print("Scipy optimized: ", scipy.optimize.brent(f))

def brent(a, b):
    x = a
    c = (a+b)/2
    
    while (True):
        
        
        R = f(b)/f(c)
        S = f(b)/f(a)
        T = f(a)/f(c)
        
        P = S*(T*(R-T)*(c-b)-(1-R)*(b-a))
        Q = (T-1)*(R-1)*(S-1)
        
        temp = b + P/Q
        
        if (np.abs(temp-x) < 2e-15):
            x = temp
            break
        x = temp
        if (temp<c):
            b = c
            c = x
        else: 
            a = c
            c = x
    
    return x

a = -2
b = 2

print("My Implementation: ", brent(a,b))