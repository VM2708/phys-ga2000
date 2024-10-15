#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:03:50 2024

@author: vedhasyamuvva
"""

import astropy.io.fits as af
import matplotlib.pyplot as plt
import numpy as np
import timeit

#Part a Plot the galaxies
hdu_list = af.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data


logwave = 10**(logwave-1)

flux = flux[0:500]

#Flux has 9713 galaxies with each galaxy having an intensity per wavelength measurement
print(np.shape(logwave))
print(np.shape(flux))

for i in range(5):
    plt.plot(logwave, flux[i], label=f'Galaxy {i+1}')
    
plt.xlabel('Wavelength (nm)')
plt.ylabel(r'Flux ($10^{-17}$ erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)')
plt.title('Spectra of a few galaxies')
plt.legend()
plt.savefig("SpectraOfAFewGalaxies.png")
plt.show()

#Part b normalize
originalflux = flux
norms = np.sum(flux,1) #holds the normalizations
print(np.shape(norms))
flux = (flux.T/norms).T

#Part c, center and save the residuals
means = np.mean(flux,0) #holds the means
flux = flux - means

#Part c,i: Plot the new graphs for fun
for i in range(3):
    plt.plot(logwave, flux[i], label=f'Galaxy {i+1}')
    
plt.xlabel('Wavelength (nm)')
plt.ylabel(r'Flux ($10^{-17}$ erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)')
plt.title('Normalized and Centered Spectra of a few galaxies')
plt.legend()
plt.savefig("NormalizedSpectraOfAFewGalaxies.png")
plt.show()

#Part d Find eigenVals/Vecs of covariance matrix
R = flux.T
cov = 1/(np.shape(flux)[0]) * R @ R.T
eigvals, eigvecs = np.linalg.eig(cov)

idx = eigvals.argsort()[::-1]  # Get indices to sort in descending order
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

for i in range (5):
    plt.plot(logwave,eigvecs[:,i], '.')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Eigenvectors of the Residuals')
plt.title('Eigenvectors')
plt.savefig("Eigenvectors.png")
plt.show()


#Part e Find eigenVals/Vecs of R matrix and compare computational cost
U,S, Vh = np.linalg.svd(R.T, full_matrices=False)
eigvecs = Vh.T
print("eigvecs: ", np.shape(eigvecs), np.shape(eigvecs[i]))

#print("vt: ", eigvecs)

covTime = timeit.timeit("np.linalg.eig(cov)", globals = globals(), number=5)
SVDTime = timeit.timeit("np.linalg.svd(R.T, full_matrices=False)", globals = globals(), number=5)
print("Time taken when using COV matrix: ", covTime)
print("Time taken when using SVD: ", SVDTime)

#Part f Determine why you would do either 
print("condition number of C: ", np.max(cov)/np.min(cov))
print("condition number of R: ", np.max(R)/np.min(R))

#Part g Do PCA with first 5 components

Nc = 5

coefficients = flux @ eigvecs

coefficients_truncated = coefficients[:, :Nc]

reconstructed_flux = coefficients_truncated @ eigvecs[:, :Nc].T

reconstructed_flux += means
reconstructed_flux = (reconstructed_flux.T * norms).T

for i in range(5): 
    plt.figure(figsize=(10, 6))

    plt.plot(logwave, originalflux[i], label=f'Original Galaxy {i+1}', alpha=0.7)

    plt.plot(logwave, reconstructed_flux[i], label=f'Reconstructed Galaxy {i+1}', linestyle='--')
    
    plt.xlabel('Wavelength (Angstroms)')
    plt.ylabel(r'Flux ($10^{-17}$ erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)')
    plt.title(f'Original vs Reconstructed Spectrum for Galaxy {i+1}')
    plt.legend()
    plt.savefig(f"ReconstructGalaxy{i}.png")
    plt.show()

#Part h Plot the various coefficients for all the galaxies
plt.figure(figsize=(8, 6))
plt.scatter(coefficients[:, 0], coefficients[:, 1], c='b', label='c0 vs c1', alpha=0.7)
plt.xlabel('c0')
plt.ylabel('c1')
plt.title('c0 vs c1')
plt.legend()
plt.savefig("c0vsc1.png")
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(coefficients[:, 0], coefficients[:, 2], c='r', label='c0 vs c2', alpha=0.7)
plt.xlabel('c0')
plt.ylabel('c2')
plt.title('c0 vs c2')
plt.legend()
plt.savefig("c0vsc2.png")
plt.show()


# Part i Calculate residuals for Nc = 1 to 20
max_Nc = 20
residuals = []

for Nc in range(1, max_Nc + 1):
    coefficients_truncated = coefficients[:, :Nc]
    reconstructed_flux = coefficients_truncated @ eigvecs[:, :Nc].T
    reconstructed_flux += means
    
    squared_residuals = np.sum((flux + means - reconstructed_flux) ** 2)
    
    rms_residual = np.sqrt(squared_residuals / np.product(np.shape(flux)))
    residuals.append(rms_residual)

plt.figure(figsize=(8, 6))
plt.plot(range(1, max_Nc + 1), residuals)
plt.xlabel('Number of Components (Nc)')
plt.ylabel('Root-Mean-Squared Residual')
plt.title('RMS Residual vs Nc')
plt.savefig("Nc.png")
plt.show()


print(f'RMS for Nc = 20: {residuals[-1]}')