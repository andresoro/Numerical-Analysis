import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

pi = np.pi
pih = pi/2

A = np.array([
    [1, 0, 0, 0],
    [1, pih, pih**2, pih**3],
    [1, 0, 0, 0],
    [1, pih, pih**2, pih**3],
    [0, 1, pi, (3*(pih)**2)],
    [0, 0, 2, 3*pi],
    [0, 1, 0, 0],
    [0, 0, pi, 0]
])

B = np.array([1, 0, 0, -1, 0, 0, 0, 0])


S = np.linalg.lstsq(A, B)
S0 = S[0]
S1 = S[3]
a0, b0, c0, d0 = S0[0], S0[1], S0[2], S0[3]
a1, b1, c1, d1 = S1[0], S1[1], S1[2], S1[3]



def spline(x):
    results = []
    for i in x:
        if i <= pih:
            results.append(
                a0 + (b0*i) + (c0*(i**2)) + (d0*(i**3)) 
            )
        if i > pih:
            results.append(
                a1 + b1*(i-pih) + (c1*(i-pih)**2) + (d1*(i-pih)**3)
            )
    return results
            
x = np.linspace(0, 2*pi, 256, endpoint=True)
a = spline(x)

plt.plot(x, np.cos(x))
plt.show()