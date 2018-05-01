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

    for k in range(0, m):
        sig = 0
        for j in xj:
            sig += f(j)*np.cos(k*j)
        ak.append((1/m)*sig)

    for k in range(0, m-1):
        sig = 0
        for j in xj:
            sig += f(j)*np.sin(k*j)
        bk.append((1/m)*sig)  

    return ak, bk

def nodes(m):
    xj = []
    
    for j in range(2*m - 1):
        n = -np.pi + (j/m)*np.pi 
        xj.append(n)
    return xj

# Discrete fourier approximaton for a given function on an interval
def fourier_approx(f, x, m):
    xj = nodes(m)
    ak, bk = coefficients(xj, m, f)

    term1 = ak[0]/2
    term2 = ak[m-1]*np.cos(m*x) 
    term3 = 0

    for k in range(1, m-1):
        s = ak[k]
        c = np.cos(k*x)

        s2 = bk[k]
        c2 = np.sin(k*x)
        term3 += (s*c + s2*c2) 

    return term1 + term2 + term3


if __name__ == '__main__':
    m = 50
    n=200
    domain = np.linspace(a, b, n)
    actual = [sigmoid(x) for x in domain]

    approx = [fourier_approx(sigmoid, x, m) for x in domain]

    plt.plot(domain, actual, 'C1', label="Actual")
    plt.plot(domain, approx, 'C2', label="Approx")
    plt.show()

    

    

