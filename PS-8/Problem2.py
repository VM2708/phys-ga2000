#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:37:11 2024

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


piano = getdata("piano.txt")
trumpet = getdata("trumpet.txt")


hz = 44100
dt = 1/hz
N = np.shape(piano)[0]

time = np.arange(0, N * dt, dt)

plt.plot(piano, ".")
plt.title("Piano Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Intensity (dec)")
plt.savefig("piano1.png")
plt.show()


plt.plot(trumpet, ".")
plt.title("Trumpet Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Intensity (dec)")
plt.savefig("trumpet1.png")
plt.show()

shiftPiano = np.abs(np.fft.rfft(piano))
freqs_piano = np.fft.rfftfreq(N, dt)
plt.plot(freqs_piano, shiftPiano, "-")
plt.title("Piano Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dec)")
plt.xlim(0, 4000)
plt.savefig("piano2zoom.png")
plt.show()

shiftPiano = np.abs(np.fft.rfft(piano))
freqs_piano = np.fft.rfftfreq(N, dt)
plt.plot(freqs_piano, shiftPiano, "-")
plt.title("Piano Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dec)")
plt.xlim(0, 10000)
plt.savefig("piano2.png")
plt.show()

shiftTrumpet = np.abs(np.fft.rfft(trumpet))
freqs_trumpet = np.fft.rfftfreq(N, dt)
plt.plot(freqs_trumpet,shiftTrumpet, "-")
plt.title("Trumpet Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dec)")
plt.xlim(0, 4000)
plt.savefig("trumpet2zoom.png")
plt.show()

shiftTrumpet = np.abs(np.fft.rfft(trumpet))
freqs_trumpet = np.fft.rfftfreq(N, dt)
plt.plot(freqs_trumpet,shiftTrumpet, "-")
plt.title("Trumpet Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity (dec)")
plt.xlim(0, 10000)
plt.savefig("trumpet2.png")
plt.show()
