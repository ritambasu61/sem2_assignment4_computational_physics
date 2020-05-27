#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:41:25 2020

@author: ritambasu
"""

import numpy as np
from matplotlib import pyplot as plt
fig, ax = plt.subplots(1, 1)

#Comparison function defined for apperently maximum EFFICIENCY
def g(x):
    return(1.28*np.exp(-0.97*x))
    #this 0.97 value is just accurate under a=1.28 for g(x)>=f(x)
    #calculated using Desmos App in Play store


x=np.random.rand(10000)
x=-np.log(abs(x))/0.97 #transformation function y(x) for my defined g(x)
y=np.random.rand(10000)*g(x)

#Error function
def f(x):
    return(np.sqrt(2/np.pi))*np.exp(-x**2/2)


#Rejection
x_good=x[y<f(x)]
y_good=y[y<f(x)]   


#plottings 
x_arr = np.linspace(0,10,1000)
ax.plot(x_arr,f(x_arr),'r-', lw=5, alpha=0.5, label='envelop of norm pdf')
plt.hist(x_good,density=True,histtype='bar',label='Box-Muller randoms')
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.suptitle('A PDF of 10,000 non-uniform gaussian deviates',x=0.5,y=-0.05)
plt.legend( loc = 'best')
plt.title('Density Histogram of Random-numbers',fontsize=20)
plt.show()

#Efficiency
print("Efficiency=",(len(x_good)/len(x))*100,"%")


#other plottings
plt.scatter(x,y,label='N.U.D of comparison function',s=5)
plt.scatter(x_good,y_good,label='N.U.D of function after rejection',s=5)
plt.plot(x_arr,f(x_arr),label='envelop of norm pdf',color='Black',lw=2)
plt.plot(x_arr,g(x_arr),label='envelop of comparison pdf',color='Black',lw=2)
plt.xlabel('xi',fontsize=17)
plt.ylabel('Functions',fontsize=17)
plt.title('Plottings of numerical technique used',fontsize=20)
plt.suptitle('N.U.D = Non-Uniform Deviates',x=0.5,y=-0.05)
plt.legend( loc = 'best')
plt.show()
