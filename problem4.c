#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
  int numpoints = 10000, i ; 
  double  rand_arr[numpoints], uniform_rand[numpoints],y[numpoints] ;
    
    

  for (i = 1; i <= numpoints; i++) 
  {
    rand_arr[i] = rand() ;
    uniform_rand[i] = rand_arr[i]/(double)RAND_MAX;  // uniform random numbers between 0 and 1
    
    if(uniform_rand[i] != 0)
    {
      y[i] = - 0.5*log((double)uniform_rand[i] );//transformation function y(x)to generate exponential non-unoform pdf
    }
    else
    {
    	y[i] = 0;
    }
  }
  // storing 10,000 non-uniform exponential pdf sampled data in prob4.txt file
  FILE *data;
  data = fopen("prob4.txt","w");
  for(i = 1;i<= numpoints; i++)
  {
  	fprintf(data, "%f\n",y[i] );
  }
  
  return 0;
    
}
