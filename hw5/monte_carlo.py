# Monte Carlo method 

import random
import math
import numpy as np
from multi_gauss import multi_gauss
from scipy import integrate

def f(x):
    return multi_gauss(x)


xmin = -1
xmax = 1
# find ymin-ymax
numSteps = 10000 
ymin = f(xmin)
ymax = ymin
for i in range(numSteps):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

# Monte Carlo
rectArea = (xmax - xmin) * (ymax - ymin)
numPoints = 10000 
ctr = 0
for j in range(numPoints):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if math.fabs(y) <= math.fabs(f(x)):
        if f(x) > 0 and y > 0 and y <= f(x):
            ctr += 1 # area over x-axis is positive
        if f(x) < 0 and y < 0 and y >= f(x):
            ctr -= 1 # area under x-axis is negative

fnArea = rectArea * float(ctr) / numPoints

print("Numerical integration = " + str(fnArea))
