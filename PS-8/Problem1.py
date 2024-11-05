#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:53:31 2024

@author: vedhasyamuvva
"""

import matplotlib.pyplot as plt
import numpy as np
import jax
import jax.numpy as jnp
import jax.scipy.optimize
import scipy.optimize as optimize


def getdata(file_path):
    # Read the data
    ages = []
    responses = []
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            age,response = line.split(",")
            ages.append(float(age))
            responses.append(int(float(response.strip())))
    
    ages = jnp.array(ages)
    responses = jnp.array(responses)
    return ages,responses

file_path = "survey.csv"
ages, responses = getdata(file_path)

def model(x, params):
    b0 = params[0]
    b1 = params[1]
    p = 1/(1+jnp.exp(-1*(b0+b1*x)))
    return(p)

def negloglike(params, *args):
    age, responses = args
    p = model(ages, params)
    nll = -jnp.sum(responses * jnp.log(p) + (1 - responses) * jnp.log(1 - p)) 
    return nll

xpath = []

def squirrel(xk):
    global xpath
    xpath.append(jnp.array(xk))

b0 = -2
b1 = .2

pst = jnp.array([b0,b1])
negloglike_grad = jax.grad(negloglike)

r = optimize.minimize(negloglike, pst, jac = negloglike_grad, args=(ages, responses), method='BFGS', tol=1e-6, callback=squirrel)
#First attempt was with Nelder-Mead

print("Optimized parameters (beta0, beta1):", r.x)
#print("Number of function evaluations:", r.nfev)
#print("Number of iterations:", r.nit)
#print("Path of optimization:", jnp.array(xpath))
print("Covariance Matrix approximated by inverse Hessian:", r.hess_inv)
print("Formal error (diagonal of Covariance matrix): ", np.sum(jnp.diagonal(r.hess_inv)))

plt.figure(figsize=(10, 6))
plt.scatter(ages, responses, color='blue', label='Survey Data')

age_range = jnp.linspace(ages.min(), ages.max(), 500)
probabilities = model(age_range, r.x)

plt.plot(age_range, probabilities, color='red', label='Logistic Model')
plt.xlabel('Age')
plt.ylabel('Probability of "Yes"')
plt.title('Logistic Regression Fit')
plt.legend()
plt.savefig('LogisticRegressionFit.png')
