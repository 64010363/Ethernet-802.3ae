import numpy as np
import math
import matplotlib.pyplot as plt
#  Generate Gaussian noise

def noise(xt, SNRdB):
    A = 1
    Tb = 0.1
    Eb = A ** 2 * Tb
    sigma = np.sqrt(0.5 * Eb * 10 ** (-SNRdB/10))
    n_t = np.random.normal(0, sigma, xt.size)
    return np.add(xt, n_t)

def main():
    mu = 0
    sigma = 1
    xt = np.array([0] * 1000)
    n_t = np.random.normal(mu, sigma, np.size(xt))
    print(np.shape(n_t))
    print(np.var(n_t))
    pass

if __name__ == "__main__":
    main()
