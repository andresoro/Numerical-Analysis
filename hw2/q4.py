import numpy as np
from matplotlib import pyplot as plt

def pn(p0, p1, n, a, b): 
    
    for i in range(20):
        r = 1 + (10**(-i))

        pnew = 0
        pn = p1 * r
        pn1 = p0 * r
        res = []
        


        for j in range(n+1):
            pnew = (a*pn) + (b*pn1)
            pn1 = pn
            pn = pnew
            res.append(pnew)
        print(pnew)
    
    return res

def pn2(p0, p1, n, a, b): 
    pnew = 0
    pn = p1
    pn1 = p0
    res = []


    for j in range(n+1):
        pnew = (a*pn) + (b*pn1)
        pn1 = pn
        pn = pnew
        res.append(pnew)
    
    return res

a = 2.0
b = 1.25
p0 = 1.0
p1 = -0.5
n = 50

res = pn(p0, p1, n , a, b)
res2 = pn2(p0, p1, n , a, b)

print(res)
print(res2)