import numpy as np

m = 2.0
b = 3.0

def func(x):
    return m*x + b

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
    while (abs(f(x)) > tol):
        x = x - (f(x) / derivative(f, x))
    return x
        
def hybrid(f, tol, a, b, N):
    t2 = tol/(10**(5))
    p = bisection(f, a, b, tol, N)
    n = newton(f, p, t2)
    return n

def test_hybrid(f, tol, a, b, N):
    i = 0
    h = None

    while h == None:
        h = bisection(g, -5, 5, t, i)
        i += 1
    print(i)


def dist(x):
    return ( ((func(x) - y0)**2) + ((x - x0)**2))

def g(x):
    return df(dist, x)

x1 = 0.0
x0 = 0.0
y0 = 1.0
t = 10**(-10)


n = newton(g, x1, t)
