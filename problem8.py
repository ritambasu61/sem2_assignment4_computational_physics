import numpy as np
from math import gamma
#In this code I have chosen n=1000000 for better convergence

#Monte_Carlo
N=1000000
dim=int(input("Give the dimention of the integration(integer value)="))

#extra dimension for comparison the function value
y=np.random.uniform(-1,1,N)

#defining the unit sphere
def f(x):
    x2=x**2
    s=sum(x2)
    if s<=1:
        return(1.0)
    else:
        return(0.0)


#counting the no.of points inside the unit sphere from randomly chosen points in a box as K        
k=1
f_arr=np.zeros(N)
f2_arr=np.zeros(N)#array to construct average of (f^2) 
for i in range(N):
    r_arr=np.random.uniform(-1,1,dim)#randomly chosen point in a box at "dim" dimension
    f_arr[i]=f(r_arr)
    f2_arr[i]=f(r_arr)**2
    if abs(y[i])<=f(r_arr):
        k+=1

#value of the integral as the probability of points 
V=2**dim
I=(V*k/N)
I_exact=(np.pi**(dim/2))/gamma(1+(dim/2)) #for Radius R=1 exact analytical result
print("Using Monte Carlo value of the numerical integral:",I)

#mean_value Monte_Carlo
f_av=sum(f_arr)/N
f_square_av=sum(f2_arr)/N
I_m_value=V*f_av
print("Using Mean value (Monte Carlo) Value of the numerical integral:",I_m_value)
print("value of the analytical integral:",I_exact)

#defining monte_carlo error (not mean value technique error)
err=np.sqrt(I*( V-I)/N)
err_mean=np.sqrt((f_square_av-(f_av**2))/N)*V
print("error in monte carlo=",err)
print("error in mean value monte carlo=",err_mean)
