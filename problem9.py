#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:47:21 2020

@author: ritambasu
"""
#In this code  n=10000000 should be used for better convergence (but it takes very long time to compute)
#for fast check please change n=10000 (please)
import numpy as np
from matplotlib import pyplot as plt
fig, ax = plt.subplots(1, 1)

#defining the given function to be sampled
def f(x):
    if 3.0<x<7.0:
        return(2.0)
    else:
        return(0.0)
#defining the pdf of the function after normalization  for comparison                
def p_f_exact(x):
    if 3.0<x<7.0:
        return(0.25)
    else:
        return(0.0)

#main construction        
nsteps = 100000
theta = 0.0
theta_arr=np.zeros(nsteps)#Markov chain vs steps
theta_prime_arr=np.zeros(nsteps)#for plotting all the points vs steps
pdf_arr=np.zeros(nsteps)#for plotting normalized pdf of the function
steps=np.zeros(nsteps)
x = np.linspace(0,9,nsteps)

for i in range(nsteps):
    theta_prime=theta+np.random.standard_normal()
    r = np.random.rand()
    pdf_arr[i]=p_f_exact(x[i])
    if f(theta)!=0.0:
        if (f(theta_prime)/f(theta))> r:
                theta = theta_prime
        else:
                    theta=theta

    else:
        theta = theta_prime
    theta_arr[i]=theta
    steps[i]=i
    theta_prime_arr[i]=theta_prime


#plotting of density histogram and comparison
ax.plot(x,pdf_arr,'r-',lw=1.5, alpha=1.0, label='actual pdf')
plt.hist(theta_arr,bins=100,density=True,fill=False,histtype='bar',label='MCMC randoms')
plt.xlim(0,9)
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.title('MCMC Density Histogram of Random-numbers',fontsize=20)
plt.suptitle('A PDF of 10,000 non-uniform deviates',x=0.5,y=-0.05)
plt.legend( loc = 'best')
plt.show()

#plottings of Markov Chain and all points
plt.scatter(steps,theta_prime_arr,marker="o",s=5,color='Green',label="other points")
plt.plot(steps,theta_arr,label="Markov chain",color='Blue')
plt.xlabel('steps',fontsize=17)
plt.ylabel(r'$\theta$ [steps]',fontsize=17)
plt.ylim(-4,10)
plt.title('Markov Chain.',fontsize=20)
plt.legend( loc = 'best')
plt.show()
