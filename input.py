import numpy as np
import matplotlib.pyplot as plt
import noise

def package_divider(raw_data:np.ndarray) -> np.ndarray:
    pass

def main():
    xt = np.array([0] * 10000)
    rt = noise.noise(xt, 0, 1)
    plt.plot(rt)
    plt.show()
    pass

if __name__ == "__main__":
    main()
