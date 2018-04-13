# Multi dimensional Gaussian distribution

import numpy as np
from matplotlib import pyplot as plt

def multi_gauss(x, mu=0, cov=np.eye(1)):
    """
    x and mu must be vectors with same dimensions
    cov is a symmetric positive definite matrix
    """

    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if not isinstance(mu, np.ndarray):
        mu = np.array(mu)

    numerator =  (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
    denominator =  1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )

    numerator = np.exp(numerator)

    return (numerator*denominator)

def test_multi_gauss():
    x = np.array([[0], [0], [0]])
    mu = np.array([[0], [0], [0]])
    cov = np.eye(3)
    print(multi_gauss(x, mu, cov))

# vectorize takes in a domain of values and returns
# vector of dimension D (x, mu)
def vectorize(domain, D):
    pass

if __name__ == '__main__':
    domain = np.linspace(-10, 10, 200)
    mu = np.array([0])
    vec = [np.array([i]) for i in domain]
    ran = [multi_gauss(i, mu, np.eye(1)) for i in vec]
    test_multi_gauss()
    #plt.plot(domain, ran)
    #plt.show()
    