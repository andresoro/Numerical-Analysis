# Multi dimensional Gaussian distribution

import numpy as np
from matplotlib import pyplot as plt

def multi_gauss(x, mu, cov):
    """
    x and mu must be vectors with same dimensions
    cov is a symmetric positive definite matrix
    """

    numerator =  (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
    denominator =  1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )

    numerator = np.exp(numerator)

    return (numerator*denominator)

def test_multi_gauss():
    x = np.array([[0], [0]])
    mu = np.array([[0], [0]])
    cov = np.eye(2)
    print(multi_gauss(x, mu, cov))

if __name__ == '__main__':
    domain = np.linspace(-5, 5, 200)
    mu = np.array([0])
    vec = [np.array([i]) for i in domain]
    ran = [multi_gauss(i, mu, np.eye(1)) for i in vec]

    plt.plot(domain, ran)
    plt.show()
    