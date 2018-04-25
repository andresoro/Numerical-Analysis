# Find the discrete Fourier Approximation for a given function y(x) on the interval
# [-pi, pi]
# y(x) is defined as the sigmoid function

import numpy as np
from matplotlib import pyplot as plt

a = -np.pi
b = np.pi
epsilon = 0.5

def sigmoid(x):
    return 1/(1 + np.exp(-x/epsilon))

# xj is the nodes to compute coefficients, m is number of iterations, f is func
# return ak, bk which are coefficients for discrete fourier series approx 
def coefficients(xj, m, f):
    ak = []
    bk = []

    sum = []
    for k in range(m):
        for j in xj:
            sum.append(
                (1/m)* f(j)*np.cos(k*j)
            )
    ak = sum


    sum = []
    for k in range(m-1):
        for j in xj:
            sum.append(
                (1/m)*f(j)*np.sin(k*j)
                )
    bk = sum


    return ak, bk

def nodes(m):
    xj = []
    
    for j in range(2*m - 1):
        n = -np.pi + (j/m)*np.pi 
        xj.append(n)
    return xj

# Discrete fourier approximaton for a given function on an interval
def fourier_approx(f, a, b):
    pass

domain = np.linspace(a, b, 100)
mapping1 = [sigmoid(x) for x in domain]
mapping2 = [sigmoid(x) for x in domain]
mapping3 = [sigmoid(x) for x in domain]




if __name__ == '__main__':
    m = 10
    nodes = nodes(m)
    ak, bk = coefficients(nodes, m, sigmoid)
    print(ak)