#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 13:24:06 2020

@author: ritambasu
"""
import timeit
import numpy as np
from matplotlib import pyplot as plt

#problem1
starttime1=timeit.default_timer() #code started as well as the timer
a=1103515245  #multiplier
c=12345        #increment  
m=2**31       #modulus
x=7          #seed i.e value of x0
n=10000    #number of random numbers specified in the questions
random_mine=np.zeros(n)
for i in range (n):
    x=(a*x+c)%m
    random_mine[i]=x
#normalizing my code generated random numbers
random_mine=np.array(random_mine)/(2**31)
starttime2=timeit.default_timer() #random number generated so my code ends
#defining uniform pdf
uniform=np.linspace(0,1,n)

#plotting in a histogram

starttime3=timeit.default_timer()
plt.hist(random_mine,density=True,histtype='bar',label='my coded randoms')
starttime4=timeit.default_timer()

plt.hist(uniform,density=True,histtype='bar',fill=False,label='actual randoms')
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.title('Q1.Density Histogram of Random-numbers',fontsize=20)
plt.suptitle('A PDF of 10,000 uniform deviates between 0 and 1',x=0.5,y=-0.001)
plt.legend()
plt.show()





#problem2
starttime5=timeit.default_timer() #numpy code started as well as the timer
random_numpy=np.random.rand(10000)
plt.hist(random_numpy,density=True,histtype='bar',label='numpy randoms')
starttime6=timeit.default_timer() 
"""numpy code ends as well as the timer(as uniforms daviates are being formed)"""
plt.hist(uniform,density=True,histtype='bar',fill=False,label='actual randoms')
plt.xlabel('xi',fontsize=17)
plt.ylabel('PDF',fontsize=17)
plt.title('Q2.Density Histogram of Numpy Random-numbers',fontsize=20)
plt.suptitle('A PDF of 10,000 uniform deviates between 0 and 1',x=0.5,y=-0.001)
plt.legend()
plt.show()



#problem3

"""for problem1
total time=time to generate numbers + time to nomalised it through plot density
here we have excluded the time difining uniform PDF part
"""
time_mine=(starttime2-starttime1)+(starttime4-starttime3)

"""for problem2
total time=time to generate numbers using numpy + time to nomalised it through plot density
here also we have excluded the time difining uniform PDF part
"""
time_numpy=(starttime6-starttime5)
print("Time taken by mycode in Problem1:",time_mine,"\nTime taken by numpy code in Problem2:",time_numpy)

