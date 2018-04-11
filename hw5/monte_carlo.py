# Monte Carlo method 

import random
import numpy as np
from multi_gauss import multi_gauss
from scipy import integrate

random.seed()

def f(x):
    x = np.array(x)
    mu = np.zeros(x.size)
    cov = np.eye(x.size)
    return multi_gauss(x, mu, cov)

def monte_carlo(f, N):
    total = 0
    for x in range(N - 1):
        x = random.randint(-1, 1)
        x = 2*(x-.5)
        total = total + f(x)
    return (2*total) / N

exact = integrate.quad(f, -1, 1)
error = abs(monte_carlo(f, 100) - exact)
total = monte_carlo(f, 100)

print("approx: ", total)
print("exact: ", exact)
print("error: ", error)