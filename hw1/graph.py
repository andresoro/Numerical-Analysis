import matplotlib.pyplot as plt
import numpy as np

# g(x) takes in an array of inputs and returns an array of outputs
def g(x):
    # a is the array of outputs, g(x) = a
    a = []
    for i in x:
        if i < np.pi:
            a.append(-1)
        else:
            a.append(1)
    return a

#np.linspace is an array of evenly spaced numbers over a specified interval
x = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
s = np.sin(x)
a = g(x)

plt.plot(x, s)
plt.plot(x, a)
plt.show()
