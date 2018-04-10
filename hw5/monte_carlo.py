# Monte Carlo method 

import random
from multi_gauss import multi_gauss

random.seed()

def f(x):
    return x**2 + 2

def monte_carlo(f, N):
    total = 0
    for x in range(N - 1):
        x = random.randint(-1, 1)
        x = 2*(x-.5)
        total = total + f(x)
    return (2*total) / N

exact = 14/3
error = abs(monte_carlo(f, 100) - exact)
total = monte_carlo(f, 100)

print("approx: ", total)
print("exact: ", exact)
print("error: ", error)