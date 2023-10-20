import numpy as np
import matplotlib.pyplot as plt
from modulation import ASK

def correlator(rt:np.ndarray, Nbits:int) -> np.ndarray:
    f = 1 / 2
    t = np.arange(0, 1, 0.0001)
    corr = np.sin(2 * np.pi * f * t)

    zt = np.array([], dtype=np.float32)
    for i in range(0, Nbits):
        i1 = i * t.size
        i2 = (i+1) * t.size
        z_tt = np.multiply(rt[i1:i2], corr) 
        zt = np.append(zt, sum(z_tt))
        
    # print(max(zt))
    return zt


def demodulation(rt:np.ndarray, Nbits:int) -> np.ndarray:
    zt = correlator(rt, Nbits)
    med = (max(zt) + min(zt)) / 2
    a_hat = np.where(zt > med, 1, 0)
    return a_hat


def main():
    bits = np.array([0,1,1,0,1,0,1,0] * 1)
    xt = ASK(bits)
    rt = correlator(xt, 8)
    plt.plot(rt)
    plt.show()
    pass

if __name__ == "__main__":
    main()
