#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:38:26 2020

@author: ritambasu
"""

import numpy as np
from scipy import stats

#Defining probability
p=np.array([1,2,3,4,5,6,5,4,3,2,1])/36

#Defining observed frequency for observations
Y1=np.array([4,10,10,13,20,18,18,11,13,14,13])#observation1
Y2=np.array([3,7,11,15,19,24,21,17,13,9,5])#observation2

#Defining total number of distinct values
n=sum(Y1)

#Defining chi^2 statistics
v1=sum((Y1-n*p)**2/(n*p))
v2=sum((Y2-n*p)**2/(n*p))
#Defining degrees of freedom for diffierent observations
k=len(p)-1

#Defining probabily to be greater than v f
p1_V_greter_v1=(1.0-stats.chi2.cdf(v1,k))*100
p2_V_greter_v2=(1.0-stats.chi2.cdf(v2,k))*100

print('probability P(V>v) for obsevation 1=',p1_V_greter_v1,'%\nprobability P(V>v) for obsevation 2=',p2_V_greter_v2,'%\nSo,')

#Results
if ( p1_V_greter_v1<1.0 or p1_V_greter_v1>99.0) and (p2_V_greter_v2<1.0 or p2_V_greter_v2>99.0):
    print('Random numbers are not sufficiently random')
elif (1.0<p1_V_greter_v1<5.0 or 95.0<p1_V_greter_v1<99.0)and (1.0<p2_V_greter_v2<5.0 or 95.0<p2_V_greter_v2<99.0):
    print('Random numbers are suspect')
elif (5.0<p1_V_greter_v1<10.0 or 90.0<p1_V_greter_v1<95.0)and (5.0<p2_V_greter_v2<10.0 or 90.0<p2_V_greter_v2<95.0):
    print('Random numbers are almost suspect')   
elif(10.0<p1_V_greter_v1<90.0)and(10.0<p2_V_greter_v2<90.0):
    print('Numbers are sufficiently random')
else:
    print('nothing can be said from 2 observation')
    
    
