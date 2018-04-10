# Multi dimensional Gaussian distribution

import numpy as np

def multi_gauss(x, mu, cov):
    """
    x and mu must be vectors with same dimensions
    cov is a symmetric positive definite matrix
    """

   numerator =  (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
   denominator =  1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )

   numerator = np.exp(numerator)

   return (numerator*denominator)