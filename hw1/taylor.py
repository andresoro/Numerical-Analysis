import numpy as np
import matplotlib.pyplot as plt



def factorial(s):
    if s <= 0:
        return 1
    else:
        return s*factorial(s-1)

def power(s, n):
    return s**n


def f(s):
    return (2*np.cos(s)) + (3*np.sin(s))


def P2Np1_sin(n, x0):
    y = 0.0
    for i in range(0,n+1):
        M=2*i+1
        nfact=factorial(M)
        term=power(x0, M) / nfact
        term2=power(-1, i)
        y=y+term*term2
    return y

def P2N_cos(n, x0):
    y = 0.0
    for i in range(0, n+1):
        M=2*i
        nfact=factorial(M)
        term=power(x0, M) / nfact
        term2=power(-1, i)
        y=y+term*term2
    return y

def PN_f(n, x0):
    return (3.0*P2Np1_sin(n, x0)) + (2*P2N_cos(n, x0))


def graph(N):

    actual = []
    approx = []

    domain = np.linspace(-2.0*np.pi, 2.0*np.pi, 256, endpoint=True)

    #get approximation and actual outputs over the domain

    for i in domain:
        actual.append(f(i))
        approx.append(PN_f(N, i))


    #graph outputs
    plt.plot(domain, actual)
    plt.plot(domain, approx)
    plt.show()


N=10
x=2
approx=PN_f(N, x)
actual=f(x)
print("x = ", x, "and N = ", N)
print("Approx: ", approx)
print("Exact: ", actual)
print("Error: ", np.absolute(actual-approx))


graph(N)
