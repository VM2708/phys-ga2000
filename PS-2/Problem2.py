#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:18:30 2024

@author: vedhasyamuvva
"""

import numpy as np
import matplotlib.pyplot as plt
import struct
"""
Problem 2
"""
    
def problem2():
    print("32-bit: ", np.float32(1) + np.float32(2**(-23)))
    print("64-bit: ", np.float64(1) + np.float64(2**(-52)))
            
    print("32-bit minimum: ", np.float32(2**(-127)))
    print("64-bit minimum: ", np.float64(2**(-1023)))
    
    print("32-bit maximum: ", np.float32(2**(2**(7)-1)+10**38))
    print("64-bit maximum: ", np.float64(2**(2**(10)-1)+8*10**307))
    
    
    

problem2()