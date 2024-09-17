#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:27:00 2024

@author: vedhasyamuvva
"""
import numpy as np
import matplotlib.pyplot as plt

"""
Problem ??? Exercise 4.2 pg 133
"""

def Quadratic_v1(a,b,c):
    a = np.float128(a)
    b = np.float128(b)
    c = np.float128(c)
    soln1 = ((-1)*b + np.sqrt(b**2-4*a*c)) / (2*a)
    soln2 = ((-1)*b - np.sqrt(b**2-4*a*c)) / (2*a)
    return soln1, soln2

def Quadratic_v2(a,b,c):
    a = np.float128(a)
    b = np.float128(b)
    c = np.float128(c)
    soln1 = (2*c) / ((-1)*b - np.sqrt(b**2-4*a*c))
    soln2 = (2*c) / ((-1)*b + np.sqrt(b**2-4*a*c))
    return soln1 ,soln2

def quadratic(a,b,c):
    a = np.float64(a)
    b = np.float64(b)
    c = np.float64(c)
    
    d = np.square(b) - 4*a*c
    
    if (d==0): return -b/(2*a)
    if (d>0):
        if (b>0):
            soln1 = (2*c)/(-b-np.sqrt(d))
            soln2 = (-b-np.sqrt(d))/(2*a)
        else:
            soln1 = (-b+np.sqrt(d))/(2*a)
            soln2 = (2*c)/(-b+np.sqrt(d))
    return soln1,soln2

def handtest(a,b,c):
    #print("v1: ", Quadratic_v1(a,b,c))
    #print("v2: ", Quadratic_v2(a,b,c))
    soln1, soln2 = quadratic(a,b,c)
    print(soln1)
    print(soln2)