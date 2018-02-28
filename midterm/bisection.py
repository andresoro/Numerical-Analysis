
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

def funct(x):
    return (x + 1)


bis = bisection(funct, -3, 3, .00000001, 100)
print(bis)

    