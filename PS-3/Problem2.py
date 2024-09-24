#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:57:43 2024

@author: vedhasyamuvva
"""
from random import random
import numpy as np
import matplotlib.pyplot as plt

def PbDecay(Pb, Bi209, dt):
    
    halfLife = 3.3*60 #half life of Pb in seconds
    
    p = 1 - 2**(-dt/halfLife)
    
    count = 0
    for i in range(Pb):
        if (random() < p):
            count += 1
    Pb -= count
    Bi209 += count
    
    return Pb, Bi209

def TiDecay(Ti, Pb, dt):
    
    halfLife = 2.2*60 #half life of Ti in seconds
    
    p = 1 - 2**(-dt/halfLife)
    
    count = 0
    for i in range(Ti):
        if (random() < p):
            count += 1
    Ti -= count
    Pb += count
    
    return Ti, Pb

def Bi213Decay(Bi213, Ti, Pb, dt):
    
    halfLife = 46*60 #Halflife of Bi213 in seconds
    
    p =  1 - 2**(-dt/halfLife)
    
    countPb = 0
    countTi = 0
    for i in range(Bi213):
        if (random() < p):
            if (random() < 0.9791):
                countPb += 1
            else: countTi += 1
            
    Bi213 -= (countPb + countTi)
    Ti = Ti + countTi
    Pb = Pb + countPb
    
    return Bi213, Ti, Pb

start = 10000
dt = 1
tmax = 20000

tpoints = np.arange(0.0,tmax,dt)
Bi213Points = np.zeros(len(tpoints),dtype=int)
TiPoints = np.zeros(len(tpoints), dtype=int)
PbPoints = np.zeros(len(tpoints), dtype=int)
Bi209Points = np.zeros(len(tpoints), dtype=int)

Bi213Points[0] = start

for i in range (len(tpoints)-1):
    Bi213 = Bi213Points[i]
    Ti = TiPoints[i]
    Pb = PbPoints[i]
    Bi209 = Bi209Points[i]
    
    Bi213, Ti, Pb = Bi213Decay(Bi213,Ti,Pb,dt)
    Ti, Pb = TiDecay(Ti, Pb, dt)
    Pb,Bi209 = PbDecay(Pb, Bi209, dt)
    
    Bi213Points[i+1] = Bi213
    TiPoints[i+1] = Ti
    PbPoints[i+1] = Pb
    Bi209Points[i+1] = Bi209
    
plt.plot(tpoints, Bi213Points, label='Bi 213')
plt.plot(tpoints, TiPoints, label='Ti')
plt.plot(tpoints, PbPoints, label='Pb')
plt.plot(tpoints, Bi209Points, label='Bi 209')
plt.legend()

plt.ylabel("# of Atoms")
plt.xlabel("Time (seconds)")
plt.title("Decay of Bi213 Atoms")

plt.savefig("DecayOfBi213Atoms.png")