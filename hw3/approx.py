import numpy as np

def f(x):
    return x**3 - 2

def df(f, x):
    h = 10.0**(-8)
    ih = complex(0.0, h)
    compx = complex(x, 0.0)
    fx = f(compx + ih)
    return np.imag(fx)/h


def bisection(f, a, b, tol, N):
    i = 1 
    fa = f(a)
    while i <= N:
        #compute Pi
        p = a + ((b - a)/2)
        fp = f(p)
        if fp == 0 or (b-a)/2 < tol:
            return p
        i += 1

        if fa*fp > 0:
            a = p
            fa = fp
        else:
            b = p

def newton(f, x, tol):
    while (abs(f(x) > tol)):
        x = x - (f(x)/df(f, x))
    return x
