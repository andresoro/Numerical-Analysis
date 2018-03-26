import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

pi = np.pi
pih = pi/2

A = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, pih, pih**2, pih**3, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, pih, pih**2, pih**3],
    [0, 1, pi, (3*(pih)**2),0 , -1, 0, 0],
    [0, 2, 3*pi, -2, 0, 0, -2, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, pi, 3*pi]
])

B = np.array([1, 0, 0, -1, 0, 0, 0, 0])

inv = np.linalg.inv(A)
X = np.matmul(inv, B)


def spline(x):
    results = []
    for i in x:  
        if i <= pih:
            results.append(
                X[0] + (X[1]*i) + (X[2]*(i**2)) + (X[3]*(i**3)) 
            )
        if i > pih:
            results.append(
                X[4] + (X[5]*(i-pih)) + (X[6]*(i-pih)**2) + (X[7]*(i-pih)**3)
            )
    return results
            

x = np.linspace(0, pi, 100)
spl = spline(x)

plt.plot(x, spl)
plt.show()