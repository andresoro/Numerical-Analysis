# Compare and contrast natural cubic spline vs radial basis function interpolation
from scipy.interpolate import Rbf as radial 
from scipy.interpolate import CubicSpline as cubic
import numpy as np
from matplotlib import pyplot as plt

# The funciton compare plots the cubic and raidal interpolation methods
# for a given function f over a evenly spaced interval n

def compare(func, n, p):
    domain = np.linspace(0, n, p)
    domain2 = np.linspace(0, n, p*10)
    mapping = [func(i) for i in domain]
    e = (n/p)*(1/10)
    
    r = radial(domain, mapping, function='gaussian', episolon=e)
    c = cubic(domain, mapping, bc_type='natural')
    
    plt.plot(domain2, func(domain2), 'g', label="Actual")
    plt.plot(domain2, r(domain2), 'b', label="Radial")
    #plt.plot(domain2, c(domain2), 'r', label="Cubic")
    plt.legend(loc='lower left')
    
    plt.show()

def f(x):
    if isinstance(x, list):
        for i in x:
            return [2*np.sin(i) for i in x]
    else:
        return 2*np.sin(x)



compare(f, np.pi, 10)