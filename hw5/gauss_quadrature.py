# Tensor product Gaussian quadrature method to approximate 
# n intergrals 
# Test on multivariate gaussian distribution 

import numpy as np
from multi_gauss import multi_gauss

def gauss_quadrature(a, b, m, n, p):
    h1 = (b - a) / 2
    h2 = (b + a) / 2
    J = 0

    for i in range(1, m):
        Jx = 0