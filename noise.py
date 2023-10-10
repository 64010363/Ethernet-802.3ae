import numpy as np
#  Generate Gaussian noise

def noise(xt, mu, sigma):
    n_t = np.random.normal(mu, sigma, np.size(xt))
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
