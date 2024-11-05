#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:06:54 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt

def getdata(file_path):
    # Read the data
    arr = []
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            arr.append(float(line))
    arr = np.array(arr)
    return arr

dow = getdata("dow.txt")
N = print(np.shape(dow))

plt.plot(dow, ".", label = "original")
plt.title("Daily Closing Value of Dow Jones Industrial Average")
plt.xlabel("Market Days since start day (days)")
plt.ylabel("Daily closing value ($) ")
plt.savefig("dow.png")


shiftDow = np.fft.rfft(dow)
shiftDowOriginal = shiftDow
print("original:", shiftDowOriginal)


N = np.shape(shiftDow)[0]
print(int(N/10))
shiftDow[int(N/10):] = np.zeros_like(shiftDow[int(N/10):])
print("first 10%:", shiftDow)

reshiftedDow = np.fft.irfft(shiftDow)
plt.plot(reshiftedDow, ".", label = "With first 10% coeff")
plt.legend()
plt.savefig("First10.png")
plt.show()


plt.plot(dow, ".", label = "original")
plt.title("Daily Closing Value of Dow Jones Industrial Average")
plt.xlabel("Market Days since start day (days)")
plt.ylabel("Daily closing value ($) ")


shiftDow = np.fft.rfft(dow)

N = np.shape(shiftDow)[0]
print(int(N/50))
shiftDow[int(N/50):] = np.zeros_like(shiftDow[int(N/50):])
print("first 2%:", shiftDow)

reshiftedDow = np.fft.irfft(shiftDow)
plt.plot(reshiftedDow, ".", label = "With first 2% coeff")
plt.legend()
plt.savefig("First2.png")
plt.show()