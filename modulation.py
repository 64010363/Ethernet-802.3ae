import numpy as np
import matplotlib.pyplot as plt

# def ASK(package:np.ndarray) -> np.ndarray:
#     f = 1 / 0.0085
#     t = np.arange(0, 1, 0.0001)
#     pulse = np.sin(2 * np.pi * f * t)
#     no_pulse = 0 * np.arange(0, 1, 0.0001)

#     signal = np.array([], dtype=np.float32)
#     for bit in package:
#         if bit == 1:
#             signal = np.append(signal, pulse)
#         else:
#             signal = np.append(signal, no_pulse)
#     return signal
def ASK(package: np.ndarray, amplitude=1, frequency=1, sample_rate=100, duration=1):
    t = np.linspace(0, len(package) * duration, int(len(package) * sample_rate * duration))
    carrier = amplitude * np.sin(2 * np.pi * frequency * t)
    n = int(sample_rate * duration)
    modulated_signal = np.zeros_like(carrier)
    # plt.plot(carrier)
    # plt.show
    i = 0  
    while i < len(package):
        bit = package[i]
        if bit == 1:
            modulated_signal[i*n : (i+1)*n] = carrier[i*n : (i+1)*n]
        i += 1 
    return modulated_signal

def main():
    # bits = np.array([0,1,1,0,1,0,1,0] * 1)
    # xt = ASK(bits)
    # plt.plot(xt)
    # plt.show()
    # pass
    data = np.array([1, 0, 0, 1, 1, 1, 0, 0, 0, 1])  
    modulated_signal = ASK(data, amplitude=1, frequency=1, sample_rate=1000, duration=1)
    plt.plot(modulated_signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('ASK Modulated Signal')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
