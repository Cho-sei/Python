# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:39:05 2018

@author: Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal

plt.close('all')

input_file = "learn_data_B.csv"
Data = np.loadtxt(input_file,delimiter=",")

data = Data[623,0:62] #読み込む行

Fs = 250
f,t,Sxx = signal.spectrogram(data,Fs,noverlap=30,nperseg=32)

plt.figure()
plt.pcolormesh(t,f,Sxx)
plt.xlim([0,0.22])
plt.ylim([0,40])
plt.xlabel("time")
plt.ylabel("frequency")
plt.colorbar()
plt.show()
