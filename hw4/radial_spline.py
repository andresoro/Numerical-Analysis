# Compare and contrast natural cubic spline vs radial basis function interpolation
from scipy.interpolate import Rbf as radial 
from scipy.interpolate import CubicSpline as cubic
import numpy as np
from matplotlib import pyplot as plt

# The funciton compare plots the cubic and raidal interpolation methods
# for a given function f over a evenly spaced interval n

def compare(func, n):
    domain = np.linspace(0, n, n+1)
    domain2 = np.linspace(0, n, n*10)
    mapping = [func(i) for i in domain]
    
    r = radial(domain, mapping, function='gaussian')
    c = cubic(domain, mapping, bc_type='natural')
    
    #plt.plot(domain2, f(domain2), 'g')
    plt.plot(domain2, r(domain2), 'b', label="Radial")
    plt.plot(domain2, c(domain2), 'r', label="Cubic")
    plt.legend(loc='lower left')
    
    plt.show()

def f(x):
    return 2*np.sin(x)



compare(f, 10)