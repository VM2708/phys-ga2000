#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:51:57 2024

@author: vedhasyamuvva
"""

#Exercise 5.15 in Newman
import matplotlib.pyplot as plt
import jax.numpy as jnp
import numpy as np
import jax

def f(x):
    return 1 + 1/2*jnp.tanh(2*x)  # Use `jnp.tanh` instead of `np.tanh` for JAX compatibility


STEP_SIZE = 0.01
xarr = np.arange(-2, 2 + STEP_SIZE, STEP_SIZE)  # Array of x-values
yarr = np.empty_like(xarr)  # Empty array for storing numerical derivatives

for i in range(np.size(xarr)): 
    x = xarr[i]
    yarr[i] = (f(x + STEP_SIZE / 2) - f(x - STEP_SIZE / 2)) / STEP_SIZE

plt.plot(xarr, yarr, 'o', label="Using Central Difference")

dfjax = jax.grad(f)
x_jax = jnp.array(xarr)  
y_jax = np.array([dfjax(x) for x in xarr])

plt.plot(xarr, y_jax, label="Using JAX")  # xarr is a standard numpy array
plt.plot(xarr, 1/jnp.cosh(2*xarr)**2, label = "Analytical derivative")

plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Derivative of f(x) = 1 + 1/2 * tanh(2x)")
plt.legend()
plt.savefig("DerivativeOfF(x).png")
plt.show()
