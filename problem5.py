#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:45:16 2020

@author: ritambasu
"""
from scipy.stats import norm
import numpy as np
from matplotlib import pyplot as plt
fig, ax = plt.subplots(1, 1)

#Box-Muller method to define y1 for random numbers of Gaussian non-uniform deviates
x1=np.random.rand(10000)
x2=np.random.rand(10000)
y=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)

#defining gaussian random numbers using scipy with mean 0 and variance 1 
r=norm.rvs(size=10000)

#defining gaussian pdf as an envelop of the histogram
x = np.linspace(-4,4,1000)
def f(x):
    return(1/np.sqrt(2*np.pi))*np.exp(-x**2/2)
    
#plottings
ax.plot(x,f(x),'r-', lw=5, alpha=0.5, label='envelop of norm pdf')
plt.hist(y,density=True,histtype='bar',label='Box-Muller randoms')
plt.hist(r, density=True, histtype='bar',fill=False, alpha=0.2,label='Scipy randoms')
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.title('Gaussian Density Histogram of Random-numbers',fontsize=20)
plt.suptitle('A PDF of 10,000 non-uniform gaussian deviates',x=0.5,y=-0.05)
plt.legend( loc = 'best')
plt.show()



