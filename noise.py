import numpy as np
import math
#  Generate Gaussian noise

def noise(xt, SNRdB):
    sigma = math.sqrt(0.5 * E)
    n_t = np.random.normal(0, sigma, np.size(xt))
    return xt + n_t

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
