#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:23:27 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit

"""
Problem 4 Exercise 3.7 pg 122
"""
""" Creates the Mandelbrot Set for a given grid size and iteration amount
 
Inputs:
 ------
 grid_size: Nummpy value
            Value to create a grid_size x grid_size grid of points to assess whether 
            a point is within the mandelbrot set or not
 L : NumPy value
     value to define how many times to iterate to check whether a point is within a mandelbrot set.

"""
def mandelbrotSet(grid_size, L):
    size = 4/grid_size
    arr = np.arange(-2,2+size,size)
    real, image = np.meshgrid(arr,arr,indexing='ij')
    
    c = real + 1j*image

    z = np.zeros_like(c)
    mask = np.ones_like(z, dtype=bool)
    
    for i in range(L):
        z[mask] = np.square(z[mask]) + c[mask]
        mask = np.abs(z) < 2

    grid = np.abs(z) <= 2
    
    x, y = np.where(grid)
    x2,y2 = np.where(np.logical_not(grid))
    
    plt.imshow(grid.T, extent=[-2, 2, -2, 2], cmap='Greys', origin='lower')
    plt.title('Mandelbrot Set')
    plt.yticks(np.arange(-2,3,1.0))
    plt.xlabel("Real Part of Complex number C")
    plt.ylabel("Imaginary Part of Complex number C")
    plt.savefig("MandelbrotSet.png")
    

mandelbrotSet(500,100)