import numpy as np
import math
import matplotlib.pyplot as plt
#  Generate AWGN noise

def noise(xt, SNRdB):
    A = 1
    Tb = 0.1
    Eb = A ** 2 * Tb
    # Increase the noise by multiplying sigma with a higher factor, e.g., 10
    sigma = np.sqrt(0.5 * Eb * 10 ** (-SNRdB/10) * 10)
    n_t = np.random.normal(0, sigma, xt.size)
    return np.add(xt, n_t)

def main():
 # Create a signal (in this case, an array of 1000 zeros)
    xt = np.array([0] * 1000)
    
    # Specify the desired SNR (in dB)
    SNRdB = 10  # You can change this to the desired SNR value

    # Generate noisy signal by adding noise to the original signal
    noisy_signal = noise(xt, SNRdB)
    
    # Create a time axis (assuming discrete time)
    time_axis = np.arange(0, len(xt))
    
    # Plot the original signal, noisy signal, and noise
    # plt.figure(figsize=(10, 6))
    # plt.plot(time_axis, xt, label="Original Signal", color="b")
    # plt.plot(time_axis, noisy_signal, label=f"Noisy Signal (SNR = {SNRdB} dB)", color="r")
    
    # Calculate and plot the noise component
    noise_component = noisy_signal - xt
    plt.plot(time_axis, noise_component, label="Noise", color="g")

    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.title("Noise")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
