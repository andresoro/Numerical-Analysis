# Tensor product Gaussian quadrature method to approximate 
# n intergrals 
# Test on multivariate gaussian distribution 

import numpy as np
from multi_gauss import multi_gauss
from matplotlib import pyplot as plt
from scipy import integrate

# recursive legendre polynomial
def legendre(n, x):
    x = np.array(x)
    if n == 0:
        return x*(0)+1
    elif n == 1:
        return x
    else: 
        return ((2*n-1)*x*legendre(n-1, x) - (n-1)*legendre(n-2, x))/n

# Derivative of legendre polynomials
def Dlegendre(n, x):
    x=np.array(x)
    if n==0:
        return x*0
    elif n==1:
        return x*0+1
    else:
        return (n/(x**2-1.0))*(x*Legendre(n,x)-Legendre(n-1,x))
    
# Roots of Legendre poly returns [x, y ] x = sample points, y = weights
def LegendreRootsAndWeights(order):
    return np.polynomial.legendre.leggauss(order)

def GLQuadrature(func, order, a, b):
    [xs, Ws] = LegendreRootsAndWeights(order)
    return  (b-a)*0.5*sum(Ws*func((b-a)*0.5*xs + (b+a)*0.5))

#define func and interval
a = -1
b = 1


deg = 8
y, w = np.polynomial.legendre.leggauss(deg)
f = [multi_gauss(i) for i in y]
gauss = sum(w * f)
print(gauss)