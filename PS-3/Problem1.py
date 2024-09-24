#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:59:58 2024

@author: vedhasyamuvva
"""

import numpy as np
import timeit
import matplotlib.pyplot as plt


def Multiply(N):
    C = np.zeros((N,N))
    A = np.random.rand(N,N)
    B = np.random.rand(N,N)
    for i in range (N):
        for j in range (N):
            for k in range (N):
                C[i,j] += (A[i,j] * B[i,j])

def dotMultiply(N):
    A = np.random.rand(N,N)
    B = np.random.rand(N,N)
    C = np.dot(A,B)
    return C

total_vals1 =20
total_vals2 = 100
x1 = np.arange(total_vals1)*10 + 10
x2 = np.arange(total_vals2)*10 + 10
y1 = np.zeros_like(x1, dtype = float)
y2 = np.zeros_like(x2, dtype = float)

for i in range (x1.size):
    y1[i] =  timeit.timeit(f"Multiply({x1[i]})", globals = globals(), number=1)
    print(i,y1[i])

for i in range (x2.size):
    y2[i] =  timeit.timeit(f"dotMultiply({x2[i]})", globals = globals(), number=1)
    print(i,y2[i])

x1 = np.log10(x1)
y1 = np.log10(y1)

x2 = np.log10(x2)
y2 = np.log10(y2)

theory1 = x1*3 - 6.07 #Manually fit to see how accurate it is
theory2 = x2*(2.1) - 7.6 #Manually fit to see how accurate it is

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(x1,y1,'o', label="Experimental Result")
axs[0].plot(x1,theory1,'-', label="Theoretical Result")
axs[0].set_title('Explicit Multiplication')
axs[0].set_xlabel("Log of Size of Matrix (log10(N))")
axs[0].set_ylabel("Log of Time elapsed (log10(sec))")
#axs[0].set_xscale("log")
#axs[0].set_yscale("log")
#axs[0].set_ylim(10**(-2.5))

axs[1].plot(x2, y2,'o')
axs[1].plot(x2,theory2,'-', label="Theoretical Result")
axs[1].set_title('Np.Dot() Multiplication')
axs[1].set_xlabel("Log of Size of Matrix (log(N))")
axs[1].set_ylabel("Log of Time elapsed (log(sec))")
#axs[1].set_xscale("log")
#axs[1].set_yscale("log")

plt.tight_layout()
plt.savefig("MatrixMultiplication.png")
print ("done")
