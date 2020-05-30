#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:01:54 2020

@author: ritambasu
"""
import emcee
import corner
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt


#extracting data from url by saving it in atext file named data.txt

lines = open('data.txt','r').read().split('\n') #making a list whose elements are each line of the data
lines=lines[5:] #cutting the headlines from the data and keeping only  the data part with '&'
index=[]
x=[]
y=[]
yerr=[]
#making those required lists
for i in range (len(lines)):
    txt=lines[i]
    index_dt,x_dt,y_dt,yerr_dt=txt.split('&')
    index.append(float(index_dt))
    x.append(float(x_dt))
    y.append(float(y_dt))
    yerr.append(float(yerr_dt))

x=np.array(x)
y=np.array(y)
yerr=np.array(yerr)


#likehood_function
def log_likelihood(theta, x, y, yerr):
    a,b,c = theta
    model = a*(x**2)+(b*x)+c
    sigma2 = yerr**2
    # actually negative ln L
    return 0.5 * np.sum((y - model) ** 2 / sigma2 +np.log(2 * np.pi * sigma2))

#prior_probability_function
def log_prior(theta):
    a,b,c = theta
    """c value limit choosing is unstable...you can choose it to be 
    positive to get minimum uncertainty"""
    if -500.0 < a < 500.0 and -500.0 < b < 500.0 and 10.0< c <1000:
        return 0.0
    return -np.inf

#posterior_function
def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return (lp - log_likelihood(theta, x, y, yerr))


#marcov_chains

#minimization of likelihhod to initialize Marcov chains
guess = (1.0, 1.0,1.0)
soln = minimize(log_likelihood,guess,args=(x, y,yerr))
#initialization of Marcov chains
nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)
#running marcov chains with emacee
sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x, y, yerr))
sampler.run_mcmc(pos, 4000)
samples = sampler.get_chain()

#plotting all chains

#a value plot
plt.plot(samples[:,:,0],color='Black',lw=0.75)
#plt.ylim(-0.01,-0.006)
plt.title('Markov Chains for parameter a ',fontsize=20)
plt.ylabel('a',fontsize=17)
plt.xlabel('steps',fontsize=17)
plt.show() 

#b value plot
plt.plot(samples[:,:,1],color='Black',lw=0.75)
#plt.ylim(3.714,3.718)
plt.title('Markov Chains for parameter b ',fontsize=20)
plt.ylabel('b',fontsize=17)
plt.xlabel('steps',fontsize=17)
plt.show() 

#c value plot
plt.plot(samples[:,:,2],color='Black',lw=0.75)
#plt.ylim(18.8325,18.8352)
plt.title('Markov Chains for parameter c',fontsize=20)
plt.ylabel('c',fontsize=17)
plt.xlabel('steps',fontsize=17)
plt.show()


#medians and standerd deviation
a_true=np.median(samples[:,:,0])
b_true=np.median(samples[:,:,1])
c_true=np.median(samples[:,:,2])

a_std=np.std(samples[:,:,0])
b_std=np.std(samples[:,:,1])
c_std=np.std(samples[:,:,2])


#corners
data= np.vstack([samples[i] for i in range(len(samples))])
fig = corner.corner(data,truths=[a_true,b_true,c_true],labels=[r"$a$", r"$b$", r"$c$",r"$\Gamma \, [\mathrm{parsec}]$"],show_titles=True, title_kwargs={"fontsize": 15}) 
plt.show()

#Randomly choosen 200 models_plotting
choose=np.random.randint(0,nwalkers*4000,200)#len(data)= no.of MCMC Chain * no.of steps
def f(abc,x):
    return(abc[0]*pow(x,2)+abc[1]*x+abc[2])
    
 
x_arr=np.linspace(40,288,350)
f_arr=[]
x_f=[]
for i in range(200):
    abc=data[choose[i]]
    plt.scatter(x_arr,f(abc,x_arr),marker="o",s=0.01,color='Orange')
    for j in range(len(x_arr)):
        x_f.append(x_arr[i])
        f_arr.append(f(abc,x_arr))
    
abc_best=np.array([a_true,b_true,c_true])    
    
plt.errorbar(x, y, yerr=yerr,fmt='o',ecolor='black',capsize=5)
plt.plot(x_arr,f(abc_best,x_arr),lw=2,color='black',label='best fitted solution')
plt.title('Data Inference and fitting',fontsize=20)
plt.xlabel('x',fontsize=15)
plt.ylabel('y(x)',fontsize=15)
plt.legend()
plt.show()


#printing best_fitted a,b,c values and standerd deviations   
print("The best fittted values of:\n\ta=",a_true,"\n\tb=",b_true,"\n\tc=",c_true)
print("one sigma uncertainties are:\n\t\u0394a=",a_std,"\n\t\u0394b=",b_std,"\n\t\u0394c=",c_std)



