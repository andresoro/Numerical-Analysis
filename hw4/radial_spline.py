# Compare and contrast natural cubic spline vs radial basis function interpolation
from scipy.interpolate import Rbf as radial 
from scipy.interpolate import CubicSpline as cubic
import numpy as np
from matplotlib import pyplot as plt

# The funciton compare plots the cubic and raidal interpolation methods
# for a given function f over a evenly spaced interval n

def compare(func, n):
    domain = np.linspace(0, n, n+1)
    mapping = [func(i) for i in domain]
    
    r = radial(domain, mapping, function='gaussian')
    
    plt.plot(domain, r(domain))
    
    plt.show()

def f(x):
    return np.sin(x)
compare(f, 20)
