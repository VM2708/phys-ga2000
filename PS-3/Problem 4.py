#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:43:07 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt
#import scipy.stats

# Create an array of Y values
def createYarr(N, num_samples=10000):
    yarr = np.zeros(num_samples)
    
    for i in range(num_samples):
        x = np.random.exponential(scale=1, size=N)
        yarr[i] = np.mean(x)  # Each y is the mean of a new x array
    return yarr

# Function to calculate statistics of Y values
def valuesOfY(yarr):
    # mean = np.mean(yarr)
    # variance = np.var(yarr)
    # skew = scipy.stats.skew(yarr)
    # kur = scipy.stats.kurtosis(yarr, fisher=True)
    # print(mean, variance, skew, kur)
    
    n = 10000
    mean = np.sum(yarr)/n
    variance = np.sum((yarr-mean)**2)/(n)
    skew = np.sum((yarr-mean)**3)/np.sum((yarr-mean)**(2))**(3/2) * n**(1/2)
    kur = ((n+1)*n*(n-1))/((n-2)*(n-3)) * np.sum((yarr-mean)**4)/(np.sum((yarr-mean)**2)**2) - (3*(n-1)**2)/((n-2)*(n-3))
    return mean, variance, skew, kur

# Plot histogram of Y values for different N
def plotY(Narr):
    meanArr = np.zeros(np.size(Narr))
    varianceArr = np.zeros(np.size(Narr))
    skewArr = np.zeros(np.size(Narr))
    kurArr = np.zeros(np.size(Narr))
    
    for i in range(np.size(Narr)):
        data = createYarr(Narr[i])
        meanArr[i], varianceArr[i], skewArr[i], kurArr[i] = valuesOfY(data)
    
    fig2, ax2 = plt.subplots(2,2, figsize=(10, 10))
    
    ax2[0,0].plot(Narr,meanArr)
    ax2[0,0].set_xlabel('N')
    ax2[0,0].set_ylabel('Mean Value')
    ax2[0,0].set_title('Mean of y for Different N')
    
    ax2[1,0].plot(Narr,varianceArr)
    ax2[1,0].set_xlabel('N')
    ax2[1,0].set_ylabel('Variance')
    ax2[1,0].set_title('Variance of y for Different N')
    
    ax2[0,1].plot(Narr,skewArr)
    ax2[0,1].plot(Narr,np.ones(np.size(Narr))*0.02)
    ax2[0,1].set_xlabel('N')
    ax2[0,1].set_ylabel('Skew')
    ax2[0,1].set_title('Skew of y for Different N')
    
    ax2[1,1].plot(Narr,kurArr)
    ax2[1,1].plot(Narr,np.ones(np.size(Narr))*0.06)
    ax2[1,1].set_xlabel('N')
    ax2[1,1].set_ylabel('Kur')
    ax2[1,1].set_title('Kurtosis of y for Different N')
    
    fig2.savefig("QuadChart.png")

def calculate_Gaussian(x):
    mean = 0 # position of the center of the curve
    sigma = 1 #standard deviation
    a = 1/(sigma*np.sqrt(2*np.pi))# Normalization Constant
    ans = a * np.exp( (-1*(x-mean)**2) / (2*sigma**2) )
    return ans

def printGaussian(N):
    yarr = createYarr(N)
    x = np.arange(-4,4,0.01)
    xarr = calculate_Gaussian(x)
    
    mean, variance, skew, kur = valuesOfY(yarr)
    
    fig, ax1 = plt.subplots()
    ax1.hist((yarr-mean)/np.sqrt(variance))
    ax2 = ax1.twinx()
    ax2.scatter(x,xarr, marker = '_', color = "black", s=7)
    ax2.yaxis.set_ticks([])
    ax2.set_yticklabels([])
    ax1.set_title(f"N = {N}")
    ax2.set_title(f"N = {N}")
    fig.savefig(f"GaussianFit{N}.png")
    
printGaussian(1000)


# Run the plot function
Narr = (np.arange(1,1000, 5))
plotY(Narr)
print(valuesOfY(createYarr(1)))



