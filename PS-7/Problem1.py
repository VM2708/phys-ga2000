#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:47:23 2024

@author: vedhasyamuvva
"""
import jax
import jax.numpy as jnp  # Use jax.numpy instead of numpy

def f(rp, mp):
    return (1-rp)**2 - mp*rp**2 - rp**3*(1-rp)**2 #1 / (rp**2) - mp / (1 - rp)**2 - rp

def fp(rp, mp):
    dfjax = jax.grad(lambda rp: f(rp, mp))  # Differentiate wrt rp, holding mp constant
    return dfjax(rp)

def rp(r, R):
    return r / R

def findSol(m, M, R, tol=1e-10):
    mp = m / M
    x1 = 0.99999999
    while True:
        temp = x1 - f(x1, mp) / fp(x1, mp)  # Newton-Raphson update
        if jnp.abs(temp - x1) < tol:  
            return temp*R  # Solution found
        x1 = temp  # Update current guess

massEarth = 5.974*10**24
massMoon = 7.348*10**22
massSun = 1.989 * 10**30
massJupiter = 1.898 * 10**27
rEM = 3.844 * 10**8
rES = 1.496 * 10**11

#For the earth and the moon
print("For the Earth and the moon: (distance from Earth)", findSol(massMoon,massEarth,rEM), " meters")

#For the earth and the sun
print("For the Earth and the Sun: (distance from Sun)", findSol(massEarth, massSun, rES ), " meters")

#For the Sun and a really large earth
print("For the Sun and a really large Earth: (distance from Sun)", findSol(massJupiter, massSun, rES), " meters")
