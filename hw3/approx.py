import numpy as np

def f(x):
    return x**3 - 2

def df(f, x):
    h = 10.0**(-8)
    ih = complex(0.0, h)
    compx = complex(x, 0.0)
    fx = f(compx + ih)
    return np.imag(fx)/h

