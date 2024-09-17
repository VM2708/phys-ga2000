#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:20:26 2024

@author: vedhasyamuvva
"""

import numpy as np
import timeit

"""
Problem 3 Exercise 2.9 pg 74
"""

""" For a input L, calculates the Madelung constant for sodium chloride. 
 
Inputs:
 ------
 L : NumPy value
     value to create a range of values. Larger L leads to a more accurate constant.
     
 Returns:
 -------
 M : Numpy value
    Madelung Constant

"""
#Exercise 2.9
def exercise2_9_withLoop(L):
    M = 0
    arr = np.arange(-L,L+1,1)
    
    for i in arr:
        for j in arr:
            for k in arr:
                add = i+j+k
                denom = np.sqrt(np.square(i)+np.square(j)+np.square(k))
                if (denom != 0):
                   if (add%2 != 0): M += np.divide(1,denom)
                   else: M -= np.divide(1,denom)
    return M

""" For a input L, calculates the Madelung constant for sodium chloride. 
 
Inputs:
 ------
 L : NumPy value
     value to create a range of values. Larger L leads to a more accurate constant.
     
 Returns:
 -------
 M : Numpy value
    Madelung Constant

"""
def exercise2_9_withoutLoop(L):
    M = 0
    arr = np.arange(-L,L+1,1)
    
    i,j,k = np.meshgrid(arr,arr,arr,indexing='ij')
    add = i+j+k
    denom = np.sqrt(np.square(i)+np.square(j)+np.square(k))
    
    denom[denom == 0] = np.inf
    denom[add % 2 == 0] = -1*denom[add % 2 == 0]
    
    M = np.sum(1/denom)
    return M

L = 70
print("Result with For Loop: ", exercise2_9_withLoop(L))
print("Result without For Loop: ", exercise2_9_withLoop(L))

withLoop = timeit.timeit("exercise2_9_withLoop(70)", globals = globals(), number=5)
withoutLoop = timeit.timeit("exercise2_9_withoutLoop(70)", globals = globals(), number=5)

print("time taken with for loop: ", withLoop)
print("time taken without for loop: ", withoutLoop)