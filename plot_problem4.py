#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:01:46 2020

@author: ritambasu
"""
import numpy as np
from matplotlib import pyplot as plt
fig, ax = plt.subplots(1, 1)

#defining exponential pdf as an envelop of the histogram
x = np.linspace(0,5,1000)
def exact_f(x):
    return(2*np.exp(-2*x))

#coverting txt file to array
y=np.loadtxt('prob4.txt')

#plottings
ax.plot(x,exact_f(x),'r-', lw=5, alpha=0.5, label='analytical envelop of exponential pdf')
plt.hist(y,bins=150,fill=False,density=True,histtype='bar',label='numerical randoms')
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.title('Exponential Density Histogram using transformtion method',fontsize=20)
plt.suptitle('A PDF of 10,000 non-uniform exponential deviates',x=0.5,y=-0.05)
plt.legend( loc = 'best')
plt.show()