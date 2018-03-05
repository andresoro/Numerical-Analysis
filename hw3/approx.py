import numpy as np

m = 1
b = 2

def func(x):
    return x**3 + x**2 + 2

def df(f, x):
    h = 10.0**(-8)
    ih = complex(0.0, h)
    compx = complex(x, 0.0)
    return np.imag(f(compx+ih))/h

def derivative(f, x):
    h = 1
    y = 0
    while h > 10**(-5):
        y = ((f(x+h) - (f(x)))/(h))
        h = h/10
    return y

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
    try:
        while (abs(f(x) > tol)):
            x = x - (f(x) / df(f, x))
    except:
        while (abs(f(x) > tol)):
            x = x - (f(x) / derivative(f, x))
    return x
        

def dist(x):
    return ( ((func(x) - y0)**2) + ((x - x0)**2))

def g(x):
    return df(dist, x)

x1 = 1
x0 = 1
y0 = 1
t = 10**(-8)


print("DF: ", df(func, 1))
derivative(func, 1)