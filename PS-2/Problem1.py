#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:54:21 2024

@author: vedhasyamuvva
"""
import numpy as np
import matplotlib.pyplot as plt
import struct
"""
Problem 1
"""
def get_bits(number):
    """For a NumPy quantity, return bit representation
    
    Inputs:
    ------
    number : NumPy value
        value to convert into list of bits
        
    Returns:
    -------
    bits : list
       list of 0 and 1 values, highest to lowest significance
    """
    bytes = number.tobytes()
    bits = []
    for byte in bytes:
        bits = bits + np.flip(np.unpackbits(np.uint8(byte)), np.uint8(0)).tolist()
    return list(reversed(bits))

def get_fbits(value):
    bitlist=get_bits(np.float32(value))
    sign = bitlist[0]
    exponent = bitlist[1:9]
    mantissa = bitlist[9:32]
    template = """{value} decimal ->
       sign = {sign} 
       exponent = {exponent} 
       mantissa = {mantissa}"""
    print(template.format(value=value, sign=sign, exponent=exponent, mantissa=mantissa))

get_fbits(np.float32(100.98763000000))

