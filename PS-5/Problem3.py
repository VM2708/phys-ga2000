#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:01:40 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt

# Read the data
file_path = "signal.dat"

times = []
signals = []
with open(file_path, 'r') as file:
    next(file)
    for line in file:
        b, t, s, e = line.split("|")
        times.append(float(t))
        signals.append(float(s))

# Convert to numpy arrays
t = np.array(times)
s = np.array(signals)

# Plot original data
fig1 = plt.figure()
plt.plot(t, s, '.', label="Original Data")
plt.xlabel("Time(s)")
plt.ylabel("Signal")
plt.title("Signal Data")
plt.savefig("Problem3a.png")
plt.show()


fig2 = plt.figure()

t_scaled = (t - np.mean(t)) / np.std(t)
plt.plot(t_scaled, s, '.', label="Rescaled Data")


def determineCoeff(A, s, label):
    U, S, Vh = np.linalg.svd(A, full_matrices=False)

    S_inv = np.diag(1 / S)
    conNum = max(S)/min(S)

    A_pi = Vh.T @ S_inv @ U.T

    # Get polynomial coefficients
    Coeff = A_pi @ s

    # Calculate fitted values and residuals
    s_fit = A @ Coeff
    residuals = s - s_fit
    
    residuals_std = np.std(residuals)

    print(f"{label} Residual std: ", residuals_std)
    print(f"{label} Condition Num: ", conNum)
    return Coeff, s_fit, residuals_std, conNum, residuals

# Function to construct higher-degree polynomial design matrix and fit
def CreateA(N, t_scaled, s):
    # Create the design matrix for a polynomial of degree N
    A = np.vander(t_scaled, N+1, increasing=True)

    # Calculate coefficients and fitted values
    Coeff, s_fit, res_std, conNum, residuals = determineCoeff(A, s, f"{N} degree Polynomial")

    # Plot the fitted polynomial
    plt.plot(t_scaled, s_fit, '.', label=f"Fitted {N}th Degree Polynomial")
    return res_std, conNum, residuals

plt.legend()
plt.xlabel("Time(s)")
plt.ylabel("Signal")
plt.title("Signal Data")

CreateA(3,t_scaled,s)
plt.legend()

plt.savefig("3rdPolyFit.png")
CreateA(25,t_scaled,s)
plt.legend()
plt.savefig("25thPolyFit.png")
#NEED TO UPDATE THIS A MATRIX SO IT IS CLOSER TO A FOURIER SERIES
w = (2*np.pi)/(max(t_scaled) - min(t_scaled))
N = 8

A = np.empty((np.size(t_scaled), 2 * N + 1))
A[:, 0] = np.ones(np.size(t_scaled))

for i in range(1, N + 1):  
    A[:, 2 * i - 1] = np.sin(i * w * t_scaled) 
    A[:, 2 * i] = np.cos(i * w * t_scaled) 

Coeff, s_fit, residuals_std, conNum, _ = determineCoeff(A,s,"Sin/Cos")
plt.plot(t_scaled, s_fit, '.', label="Sin/Cos fit")
plt.legend()
plt.savefig("SinCosFit.png")
plt.show()

res_std, conNum, residuals = CreateA(3,t_scaled,s)
fig5 = plt.figure()

plt.plot(t_scaled, residuals, '.')
plt.xlabel("Time(s)")
plt.ylabel("Residual Signal")
plt.title("Residual Signal Data for 3rd Degree Polyomial")
plt.savefig("residual.png")

