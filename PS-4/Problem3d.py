#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:27:47 2024

@author: vedhasyamuvva
"""

import numpy as np
import math

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

def wavefunction(n, x):
    return 1 / (np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi))) * H(n, x)

def f(x, n):
    return x**2 * wavefunction(n, x)**2


def uncertainty(n):
    N = 30
    
    #x contains sample points and w contains the weights
    x,w = np.polynomial.hermite.hermgauss(N)
    
    s = 0.0
    
    for k in range(N):
        s+= w[k] * f(x[k], n)
        
    print("sqrt(x): ", np.sqrt(s))    
    uncertainty = np.sqrt(11/2) - np.sqrt(s)
    return uncertainty


print("uncertainty using Gaussian-Hermite quadrature ", uncertainty(5))
