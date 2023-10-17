import numpy as np
import matplotlib.pyplot as plt

def ASK(package:np.ndarray) -> np.ndarray:
    f = 1 / 0.0085
    t = np.arange(0, 1, 0.0001)
    pulse = np.sin(2 * np.pi * f * t)
    no_pulse = 0 * np.arange(0, 1, 0.0001)

    signal = np.array([], dtype=np.float32)
    for bit in package:
        if bit == 1:
            signal = np.append(signal, pulse)
        else:
            signal = np.append(signal, no_pulse)
    return signal

def main():
    bits = np.array([0,1,1,0,1,0,1,0] * 1)
    xt = ASK(bits)
    plt.plot(xt)
    plt.show()
    pass

if __name__ == "__main__":
    main()
