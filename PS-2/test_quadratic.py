#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:31:21 2024

@author: vedhasyamuvva
"""

import pytest
import numpy as np
import quadratic

def test_quadratic():
    # Check a simpler case (note it requires the + solution first)
    x1, x2 = quadratic.quadratic(a=1., b=8., c=12.)
    print(x1,x2)
    assert (np.abs(x1 - (- 2.)) < 1.e-10)
    assert (np.abs(x2 - (- 6)) < 1.e-10)
    
    # Check the case from the problem
    x1, x2 = quadratic.quadratic(a=0.001, b=1000., c=0.001)
    print(x1,x2)
    assert (np.abs(x1 - (- 1.e-6)) < 1.e-10)
    assert (np.abs(x2 - (- 0.999999999999e+6)) < 1.e-10)
    
    #Check a similar case
    x1, x2 = quadratic.quadratic(a=0.001, b=-1000., c=0.001)
    print(x1,x2)
    assert (np.abs(x1 - (0.999999999999e+6)) < 1.e-10)
    assert (np.abs(x2 - (1.e-6)) < 1.e-10)
    
    

test_quadratic()
