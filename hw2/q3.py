import numpy as np

def f(x):
    return ((x**4)**(1/3))

def fprime(x):
    return (4/3)*(x**(1/3))

def m1(x, h):
    return ((f(x+h) - (f(x)))/(h))

def m2(x, h):
    return ((f(x+h) - (f(x-h)))/(2*h))

def m3(x, h):
    return ((-1*f(x+(2*h)) + 4*f(x+h) - 3*f(x))/(2*h))

def m4(x, h):
    return ((f(x-2*h) - 4*f(x-h) + 3*f(x))/(2*h))

x = 1
h=1.0
while h > 10**(-14):
    print("x: ", x)
    print("h: ", h)
    print("Acutal", fprime(x))
    print("M1: ", m1(x, h), "Error: ", fprime(x) - m1(x, h))
    print("M2: ", m2(x, h), "Error: ", fprime(x) - m2(x, h))
    print("M3: ", m3(x, h), "Error: ", fprime(x) - m3(x, h))
    print("M4: ", m4(x, h), "Error: ", fprime(x) - m4(x, h))
    print("")
    h=h/10