#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:00:46 2024

@author: vedhasyamuvva
"""

from random import random
import numpy as np
import matplotlib.pyplot as plt

start = 1000

dt = 1

tao = 3.053 * 60
whenAtomDecays=np.log(1-np.random.rand(start))*tao/(-np.log(2))
sortedArr = np.sort(whenAtomDecays)

time = np.arange(0,1000,0.1)
NumDecayed = np.zeros(np.size(time))

for t in sortedArr:
    NumDecayed[np.where(time>t)] += 1

#plt.plot(time, NumDecayed, label = "Lead 208") #???
plt.plot(time, start - NumDecayed, label = "Thallium 208")

plt.ylabel("# of Thallium Atoms")
plt.xlabel("TIme to decay (seconds)")
plt.title("Decay rate of Thallium 208")
plt.legend()
plt.savefig("DecayOfThallium.png")


