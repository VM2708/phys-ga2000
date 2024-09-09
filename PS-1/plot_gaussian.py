#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:07:52 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt


def calculate_Gaussian(x):
    b = 0 # position of the center of the curve
    c = 3 #standard deviation
    a = np.sqrt(2*np.pi*c**2) # Normalization Constant
    ans = (a * np.exp( (-(x-b)**2) / (2*c**2) ))
    return ans

# create x values to be plotted
STEP_SIZE = 0.002 # step size of function
xarray = np.arange(-10, 10, STEP_SIZE, dtype=np.float32)
plt.plot(xarray, calculate_Gaussian(xarray))
plt.title("Gaussian")
plt.xlabel("bro")
plt.text(-7.5,.1,r'bro')
plt.savefig('gaussian.png')

#What does normalizing mean???