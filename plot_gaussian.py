#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:07:52 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_Gaussian(x):
    mean = 0 # position of the center of the curve
    sigma = 3 #standard deviation
    a = 1/(sigma*np.sqrt(2*np.pi)) # Normalization Constant
    ans = (a * np.exp( (-1/2*(x-mean)**2) / (sigma**2) ))
    return ans

# create x values to be plotted
STEP_SIZE = 0.002 # step size of function
xarray = np.arange(-10, 10+STEP_SIZE, STEP_SIZE, dtype=np.float32)
plt.plot(xarray, calculate_Gaussian(xarray))
plt.title("Gaussian")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.savefig('gaussian.png')

print(calculate_Gaussian(0))

#What does normalizing mean???