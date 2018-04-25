# Multi dimensional Gaussian distribution

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits import mplot3d

def multi_gauss(x):
    """
    x and mu must be vectors with same dimensions
    cov is a symmetric positive definite matrix
    """
    x = np.array(x)
  
    mu = np.zeros(x.size)
    cov = np.eye(x.size)
    np.fill_diagonal(cov, 0.1)
    

    numerator =  (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
    denominator =  1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )

    numerator = np.exp(numerator)

    return (numerator*denominator)

def test_multi_gauss():
    x = np.linspace(-1, 1, 100)
    y = [multi_gauss(i) for i in x]
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    test_multi_gauss()
    
   